# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.classes.cls_basicclass import BasicClass
from ..types.partial.classes.cls_basicclass import PartialBasicClass
from baml_core.stream import AsyncStream
from typing import Callable, Protocol, runtime_checkable


import typing

import pytest
from contextlib import contextmanager
from unittest import mock

ImplName = typing.Literal["version"]

T = typing.TypeVar("T", bound=typing.Callable[..., typing.Any])
CLS = typing.TypeVar("CLS", bound=type)


INamedfuncOutput = str

@runtime_checkable
class INamedfunc(Protocol):
    """
    This is the interface for a function.

    Args:
        name: BasicClass
        address: str

    Returns:
        str
    """

    async def __call__(self, *, name: BasicClass, address: str) -> str:
        ...

   

@runtime_checkable
class INamedfuncStream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        name: BasicClass
        address: str

    Returns:
        AsyncStream[str, str]
    """

    def __call__(self, *, name: BasicClass, address: str
) -> AsyncStream[str, str]:
        ...
class BAMLNamedfuncImpl:
    async def run(self, *, name: BasicClass, address: str) -> str:
        ...
    
    def stream(self, *, name: BasicClass, address: str
) -> AsyncStream[str, str]:
        ...

class IBAMLNamedfunc:
    def register_impl(
        self, name: ImplName
    ) -> typing.Callable[[INamedfunc, INamedfuncStream], None]:
        ...

    async def __call__(self, *, name: BasicClass, address: str) -> str:
        ...

    def stream(self, *, name: BasicClass, address: str
) -> AsyncStream[str, str]:
        ...

    def get_impl(self, name: ImplName) -> BAMLNamedfuncImpl:
        ...

    @contextmanager
    def mock(self) -> typing.Generator[mock.AsyncMock, None, None]:
        """
        Utility for mocking the NamedfuncInterface.

        Usage:
            ```python
            # All implementations are mocked.

            async def test_logic() -> None:
                with baml.Namedfunc.mock() as mocked:
                    mocked.return_value = ...
                    result = await NamedfuncImpl(...)
                    assert mocked.called
            ```
        """
        ...

    @typing.overload
    def test(self, test_function: T) -> T:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the NamedfuncInterface.

        Args:
            test_function : T
                The test function to be decorated.

        Usage:
            ```python
            # All implementations will be tested.

            @baml.Namedfunc.test
            async def test_logic(NamedfuncImpl: INamedfunc) -> None:
                result = await NamedfuncImpl(...)
            ```
        """
        ...

    @typing.overload
    def test(self, *, exclude_impl: typing.Iterable[ImplName] = [], stream: bool = False) -> pytest.MarkDecorator:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the NamedfuncInterface.

        Args:
            exclude_impl : Iterable[ImplName]
                The names of the implementations to exclude from testing.
            stream: bool
                If set, will return a streamable version of the test function.

        Usage:
            ```python
            # All implementations except the given impl will be tested.

            @baml.Namedfunc.test(exclude_impl=["implname"])
            async def test_logic(NamedfuncImpl: INamedfunc) -> None:
                result = await NamedfuncImpl(...)
            ```

            ```python
            # Streamable version of the test function.

            @baml.Namedfunc.test(stream=True)
            async def test_logic(NamedfuncImpl: INamedfuncStream) -> None:
                async for result in NamedfuncImpl(...):
                    ...
            ```
        """
        ...

    @typing.overload
    def test(self, test_class: typing.Type[CLS]) -> typing.Type[CLS]:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the NamedfuncInterface.

        Args:
            test_class : Type[CLS]
                The test class to be decorated.

        Usage:
        ```python
        # All implementations will be tested in every test method.

        @baml.Namedfunc.test
        class TestClass:
            def test_a(self, NamedfuncImpl: INamedfunc) -> None:
                ...
            def test_b(self, NamedfuncImpl: INamedfunc) -> None:
                ...
        ```
        """
        ...

BAMLNamedfunc: IBAMLNamedfunc
