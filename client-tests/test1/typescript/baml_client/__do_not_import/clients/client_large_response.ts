// This file is generated by the BAML compiler.
// Do not edit this file directly.
// Instead, edit the BAML files and recompile.

// eslint-disable-next-line @typescript-eslint/no-unused-vars
// @ts-nocheck
// @ts-ignore
// prettier-ignore

from baml_core.provider_manager import LLMManager


const LARGE_RESPONSE = LLMManager.add_llm(
    {
    name: "LARGE_RESPONSE",
    provider: "baml-openai-chat",
    retry_policy: None,
    redactions: ["api_key", ],
    options: {
        model: "gpt-3.5-turbo",
        api_key: process.env.OPENAI_API_KEY,
        request_timeout: 45,
        max_tokens: 400,
    },
    }
)
