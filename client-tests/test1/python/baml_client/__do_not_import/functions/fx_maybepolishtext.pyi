# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.classes.cls_conversation import Conversation
from ..types.classes.cls_message import Message
from ..types.classes.cls_proposedmessage import ProposedMessage
from ..types.enums.enm_messagesender import MessageSender
from ..types.partial.classes.cls_conversation import PartialConversation
from ..types.partial.classes.cls_message import PartialMessage
from ..types.partial.classes.cls_proposedmessage import PartialProposedMessage
from baml_core.stream import AsyncStream
from typing import Callable, Protocol, runtime_checkable


import typing

import pytest
from contextlib import contextmanager
from unittest import mock

ImplName = typing.Literal["v1", "v2", "v3"]

T = typing.TypeVar("T", bound=typing.Callable[..., typing.Any])
CLS = typing.TypeVar("CLS", bound=type)


IMaybePolishTextOutput = str

@runtime_checkable
class IMaybePolishText(Protocol):
    """
    This is the interface for a function.

    Args:
        arg: ProposedMessage

    Returns:
        str
    """

    async def __call__(self, arg: ProposedMessage, /) -> str:
        ...

   

@runtime_checkable
class IMaybePolishTextStream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        arg: ProposedMessage

    Returns:
        AsyncStream[str, str]
    """

    def __call__(self, arg: ProposedMessage, /) -> AsyncStream[str, str]:
        ...
class BAMLMaybePolishTextImpl:
    async def run(self, arg: ProposedMessage, /) -> str:
        ...
    
    def stream(self, arg: ProposedMessage, /) -> AsyncStream[str, str]:
        ...

class IBAMLMaybePolishText:
    def register_impl(
        self, name: ImplName
    ) -> typing.Callable[[IMaybePolishText, IMaybePolishTextStream], None]:
        ...

    async def __call__(self, arg: ProposedMessage, /) -> str:
        ...

    def stream(self, arg: ProposedMessage, /) -> AsyncStream[str, str]:
        ...

    def get_impl(self, name: ImplName) -> BAMLMaybePolishTextImpl:
        ...

    @contextmanager
    def mock(self) -> typing.Generator[mock.AsyncMock, None, None]:
        """
        Utility for mocking the MaybePolishTextInterface.

        Usage:
            ```python
            # All implementations are mocked.

            async def test_logic() -> None:
                with baml.MaybePolishText.mock() as mocked:
                    mocked.return_value = ...
                    result = await MaybePolishTextImpl(...)
                    assert mocked.called
            ```
        """
        ...

    @typing.overload
    def test(self, test_function: T) -> T:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the MaybePolishTextInterface.

        Args:
            test_function : T
                The test function to be decorated.

        Usage:
            ```python
            # All implementations will be tested.

            @baml.MaybePolishText.test
            async def test_logic(MaybePolishTextImpl: IMaybePolishText) -> None:
                result = await MaybePolishTextImpl(...)
            ```
        """
        ...

    @typing.overload
    def test(self, *, exclude_impl: typing.Iterable[ImplName] = [], stream: bool = False) -> pytest.MarkDecorator:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the MaybePolishTextInterface.

        Args:
            exclude_impl : Iterable[ImplName]
                The names of the implementations to exclude from testing.
            stream: bool
                If set, will return a streamable version of the test function.

        Usage:
            ```python
            # All implementations except the given impl will be tested.

            @baml.MaybePolishText.test(exclude_impl=["implname"])
            async def test_logic(MaybePolishTextImpl: IMaybePolishText) -> None:
                result = await MaybePolishTextImpl(...)
            ```

            ```python
            # Streamable version of the test function.

            @baml.MaybePolishText.test(stream=True)
            async def test_logic(MaybePolishTextImpl: IMaybePolishTextStream) -> None:
                async for result in MaybePolishTextImpl(...):
                    ...
            ```
        """
        ...

    @typing.overload
    def test(self, test_class: typing.Type[CLS]) -> typing.Type[CLS]:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the MaybePolishTextInterface.

        Args:
            test_class : Type[CLS]
                The test class to be decorated.

        Usage:
        ```python
        # All implementations will be tested in every test method.

        @baml.MaybePolishText.test
        class TestClass:
            def test_a(self, MaybePolishTextImpl: IMaybePolishText) -> None:
                ...
            def test_b(self, MaybePolishTextImpl: IMaybePolishText) -> None:
                ...
        ```
        """
        ...

BAMLMaybePolishText: IBAMLMaybePolishText
