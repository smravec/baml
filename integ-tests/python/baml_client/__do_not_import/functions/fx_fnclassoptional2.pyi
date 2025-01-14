# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.classes.cls_classoptionalfields import ClassOptionalFields
from ..types.partial.classes.cls_classoptionalfields import PartialClassOptionalFields
from baml_core.stream import AsyncStream
from typing import Callable, Protocol, runtime_checkable


import typing

import pytest
from contextlib import contextmanager
from unittest import mock

ImplName = typing.Literal["v1"]

T = typing.TypeVar("T", bound=typing.Callable[..., typing.Any])
CLS = typing.TypeVar("CLS", bound=type)


IFnClassOptional2Output = str

@runtime_checkable
class IFnClassOptional2(Protocol):
    """
    This is the interface for a function.

    Args:
        arg: ClassOptionalFields

    Returns:
        str
    """

    async def __call__(self, arg: ClassOptionalFields, /) -> str:
        ...

   

@runtime_checkable
class IFnClassOptional2Stream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        arg: ClassOptionalFields

    Returns:
        AsyncStream[str, str]
    """

    def __call__(self, arg: ClassOptionalFields, /) -> AsyncStream[str, str]:
        ...
class BAMLFnClassOptional2Impl:
    async def run(self, arg: ClassOptionalFields, /) -> str:
        ...
    
    def stream(self, arg: ClassOptionalFields, /) -> AsyncStream[str, str]:
        ...

class IBAMLFnClassOptional2:
    def register_impl(
        self, name: ImplName
    ) -> typing.Callable[[IFnClassOptional2, IFnClassOptional2Stream], None]:
        ...

    async def __call__(self, arg: ClassOptionalFields, /) -> str:
        ...

    def stream(self, arg: ClassOptionalFields, /) -> AsyncStream[str, str]:
        ...

    def get_impl(self, name: ImplName) -> BAMLFnClassOptional2Impl:
        ...

    @contextmanager
    def mock(self) -> typing.Generator[mock.AsyncMock, None, None]:
        """
        Utility for mocking the FnClassOptional2Interface.

        Usage:
            ```python
            # All implementations are mocked.

            async def test_logic() -> None:
                with baml.FnClassOptional2.mock() as mocked:
                    mocked.return_value = ...
                    result = await FnClassOptional2Impl(...)
                    assert mocked.called
            ```
        """
        ...

    @typing.overload
    def test(self, test_function: T) -> T:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the FnClassOptional2Interface.

        Args:
            test_function : T
                The test function to be decorated.

        Usage:
            ```python
            # All implementations will be tested.

            @baml.FnClassOptional2.test
            async def test_logic(FnClassOptional2Impl: IFnClassOptional2) -> None:
                result = await FnClassOptional2Impl(...)
            ```
        """
        ...

    @typing.overload
    def test(self, *, exclude_impl: typing.Iterable[ImplName] = [], stream: bool = False) -> pytest.MarkDecorator:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the FnClassOptional2Interface.

        Args:
            exclude_impl : Iterable[ImplName]
                The names of the implementations to exclude from testing.
            stream: bool
                If set, will return a streamable version of the test function.

        Usage:
            ```python
            # All implementations except the given impl will be tested.

            @baml.FnClassOptional2.test(exclude_impl=["implname"])
            async def test_logic(FnClassOptional2Impl: IFnClassOptional2) -> None:
                result = await FnClassOptional2Impl(...)
            ```

            ```python
            # Streamable version of the test function.

            @baml.FnClassOptional2.test(stream=True)
            async def test_logic(FnClassOptional2Impl: IFnClassOptional2Stream) -> None:
                async for result in FnClassOptional2Impl(...):
                    ...
            ```
        """
        ...

    @typing.overload
    def test(self, test_class: typing.Type[CLS]) -> typing.Type[CLS]:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the FnClassOptional2Interface.

        Args:
            test_class : Type[CLS]
                The test class to be decorated.

        Usage:
        ```python
        # All implementations will be tested in every test method.

        @baml.FnClassOptional2.test
        class TestClass:
            def test_a(self, FnClassOptional2Impl: IFnClassOptional2) -> None:
                ...
            def test_b(self, FnClassOptional2Impl: IFnClassOptional2) -> None:
                ...
        ```
        """
        ...

BAMLFnClassOptional2: IBAMLFnClassOptional2
