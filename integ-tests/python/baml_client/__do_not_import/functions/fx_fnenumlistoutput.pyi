# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.enums.enm_enumoutput import EnumOutput
from baml_core.stream import AsyncStream
from typing import Callable, List, Protocol, runtime_checkable


import typing

import pytest
from contextlib import contextmanager
from unittest import mock

ImplName = typing.Literal["v1"]

T = typing.TypeVar("T", bound=typing.Callable[..., typing.Any])
CLS = typing.TypeVar("CLS", bound=type)


IFnEnumListOutputOutput = List[EnumOutput]

@runtime_checkable
class IFnEnumListOutput(Protocol):
    """
    This is the interface for a function.

    Args:
        arg: str

    Returns:
        List[EnumOutput]
    """

    async def __call__(self, arg: str, /) -> List[EnumOutput]:
        ...

   

@runtime_checkable
class IFnEnumListOutputStream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        arg: str

    Returns:
        AsyncStream[List[EnumOutput], List[EnumOutput]]
    """

    def __call__(self, arg: str, /) -> AsyncStream[List[EnumOutput], List[EnumOutput]]:
        ...
class BAMLFnEnumListOutputImpl:
    async def run(self, arg: str, /) -> List[EnumOutput]:
        ...
    
    def stream(self, arg: str, /) -> AsyncStream[List[EnumOutput], List[EnumOutput]]:
        ...

class IBAMLFnEnumListOutput:
    def register_impl(
        self, name: ImplName
    ) -> typing.Callable[[IFnEnumListOutput, IFnEnumListOutputStream], None]:
        ...

    async def __call__(self, arg: str, /) -> List[EnumOutput]:
        ...

    def stream(self, arg: str, /) -> AsyncStream[List[EnumOutput], List[EnumOutput]]:
        ...

    def get_impl(self, name: ImplName) -> BAMLFnEnumListOutputImpl:
        ...

    @contextmanager
    def mock(self) -> typing.Generator[mock.AsyncMock, None, None]:
        """
        Utility for mocking the FnEnumListOutputInterface.

        Usage:
            ```python
            # All implementations are mocked.

            async def test_logic() -> None:
                with baml.FnEnumListOutput.mock() as mocked:
                    mocked.return_value = ...
                    result = await FnEnumListOutputImpl(...)
                    assert mocked.called
            ```
        """
        ...

    @typing.overload
    def test(self, test_function: T) -> T:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the FnEnumListOutputInterface.

        Args:
            test_function : T
                The test function to be decorated.

        Usage:
            ```python
            # All implementations will be tested.

            @baml.FnEnumListOutput.test
            async def test_logic(FnEnumListOutputImpl: IFnEnumListOutput) -> None:
                result = await FnEnumListOutputImpl(...)
            ```
        """
        ...

    @typing.overload
    def test(self, *, exclude_impl: typing.Iterable[ImplName] = [], stream: bool = False) -> pytest.MarkDecorator:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the FnEnumListOutputInterface.

        Args:
            exclude_impl : Iterable[ImplName]
                The names of the implementations to exclude from testing.
            stream: bool
                If set, will return a streamable version of the test function.

        Usage:
            ```python
            # All implementations except the given impl will be tested.

            @baml.FnEnumListOutput.test(exclude_impl=["implname"])
            async def test_logic(FnEnumListOutputImpl: IFnEnumListOutput) -> None:
                result = await FnEnumListOutputImpl(...)
            ```

            ```python
            # Streamable version of the test function.

            @baml.FnEnumListOutput.test(stream=True)
            async def test_logic(FnEnumListOutputImpl: IFnEnumListOutputStream) -> None:
                async for result in FnEnumListOutputImpl(...):
                    ...
            ```
        """
        ...

    @typing.overload
    def test(self, test_class: typing.Type[CLS]) -> typing.Type[CLS]:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the FnEnumListOutputInterface.

        Args:
            test_class : Type[CLS]
                The test class to be decorated.

        Usage:
        ```python
        # All implementations will be tested in every test method.

        @baml.FnEnumListOutput.test
        class TestClass:
            def test_a(self, FnEnumListOutputImpl: IFnEnumListOutput) -> None:
                ...
            def test_b(self, FnEnumListOutputImpl: IFnEnumListOutput) -> None:
                ...
        ```
        """
        ...

BAMLFnEnumListOutput: IBAMLFnEnumListOutput
