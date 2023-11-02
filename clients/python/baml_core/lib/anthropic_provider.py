import anthropic
import typing

from .._impl.provider import LLMProvider, register_llm_provider, LLMResponse


def __hydrate_anthropic_tokenizer() -> None:
    # Anthropic's tokenizer is a bit slow to load, so we do it here
    # to avoid the first call to run_prompt being slow.
    # Calling this multiple times is fine, as it's a no-op if the
    # tokenizer is already loaded.
    anthropic.Client().get_tokenizer()


@register_llm_provider("anthropic")
@typing.final
class AnthropicProvider(LLMProvider):
    __kwargs: typing.Dict[str, typing.Any]

    def _to_error_code(self, e: BaseException) -> typing.Optional[int]:
        if isinstance(e, anthropic.APIStatusError):
            return e.status_code
        return None

    def __init__(
        self, *, options: typing.Dict[str, typing.Any], **kwargs: typing.Any
    ) -> None:
        __hydrate_anthropic_tokenizer()

        if "max_retries" in options and "retry" in kwargs:
            assert (
                False
            ), "Either use max_retries with Anthropic via options or retry via BAML, not both"

        super().__init__(
            chat_to_prompt=lambda chat: "".join(
                map(
                    lambda c: f'{anthropic.HUMAN_PROMPT if  c["role"] != "system" else anthropic.AI_PROMPT} {c["content"]}',
                    chat,
                )
            )
            + anthropic.AI_PROMPT,
            **kwargs,
        )

        if "max_tokens_to_sample" not in options:
            # Anthropic requires a max_tokens_to_sample arg
            # We
            options["max_tokens_to_sample"] = 1000

        client_arg_names = [
            "api_key",
            "auth_token",
            "base_url",
            "timeout",
            "default_headers",
            "default_query",
            "transport",
            "proxies",
            "connection_pool_limits",
            "_strict_response_validation",
            "max_retries",
        ]
        client_kwargs = {k: options.pop(k) for k in client_arg_names if k in options}
        # Default to 0 retries if not specified.
        if "max_retries" not in client_kwargs:
            client_kwargs["max_retries"] = 0

        self.__client = anthropic.AsyncAnthropic(**client_kwargs)
        self.__client_kwargs = client_kwargs
        self.__caller_kwargs = options

    async def _run(self, prompt: str) -> LLMResponse:
        self._log_args(**self.__caller_kwargs, **self.__client_kwargs)
        prompt_tokens = await self.__client.count_tokens(prompt)
        response = typing.cast(
            anthropic.types.Completion,
            await self.__client.completions.create(
                prompt=prompt, **self.__caller_kwargs
            ),
        )
        output_tokens = await self.__client.count_tokens(response.completion)

        return LLMResponse(
            generated=response.completion,
            model_name=response.model,
            meta=dict(
                prompt_tokens=prompt_tokens,
                output_tokens=output_tokens,
                total_tokens=prompt_tokens + output_tokens,
            ),
        )