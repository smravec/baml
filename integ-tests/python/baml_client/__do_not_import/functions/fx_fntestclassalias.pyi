# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.classes.cls_testclassalias import TestClassAlias
from ..types.partial.classes.cls_testclassalias import PartialTestClassAlias
from baml_core.stream import AsyncStream
from typing import Callable, Protocol, runtime_checkable


import typing

import pytest
from contextlib import contextmanager
from unittest import mock

ImplName = typing.Literal["v1"]

T = typing.TypeVar("T", bound=typing.Callable[..., typing.Any])
CLS = typing.TypeVar("CLS", bound=type)


IFnTestClassAliasOutput = TestClassAlias

@runtime_checkable
class IFnTestClassAlias(Protocol):
    """
    This is the interface for a function.

    Args:
        arg: str

    Returns:
        TestClassAlias
    """

    async def __call__(self, arg: str, /) -> TestClassAlias:
        ...

   

@runtime_checkable
class IFnTestClassAliasStream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        arg: str

    Returns:
        AsyncStream[TestClassAlias, PartialTestClassAlias]
    """

    def __call__(self, arg: str, /) -> AsyncStream[TestClassAlias, PartialTestClassAlias]:
        ...
class BAMLFnTestClassAliasImpl:
    async def run(self, arg: str, /) -> TestClassAlias:
        ...
    
    def stream(self, arg: str, /) -> AsyncStream[TestClassAlias, PartialTestClassAlias]:
        ...

class IBAMLFnTestClassAlias:
    def register_impl(
        self, name: ImplName
    ) -> typing.Callable[[IFnTestClassAlias, IFnTestClassAliasStream], None]:
        ...

    async def __call__(self, arg: str, /) -> TestClassAlias:
        ...

    def stream(self, arg: str, /) -> AsyncStream[TestClassAlias, PartialTestClassAlias]:
        ...

    def get_impl(self, name: ImplName) -> BAMLFnTestClassAliasImpl:
        ...

    @contextmanager
    def mock(self) -> typing.Generator[mock.AsyncMock, None, None]:
        """
        Utility for mocking the FnTestClassAliasInterface.

        Usage:
            ```python
            # All implementations are mocked.

            async def test_logic() -> None:
                with baml.FnTestClassAlias.mock() as mocked:
                    mocked.return_value = ...
                    result = await FnTestClassAliasImpl(...)
                    assert mocked.called
            ```
        """
        ...

    @typing.overload
    def test(self, test_function: T) -> T:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the FnTestClassAliasInterface.

        Args:
            test_function : T
                The test function to be decorated.

        Usage:
            ```python
            # All implementations will be tested.

            @baml.FnTestClassAlias.test
            async def test_logic(FnTestClassAliasImpl: IFnTestClassAlias) -> None:
                result = await FnTestClassAliasImpl(...)
            ```
        """
        ...

    @typing.overload
    def test(self, *, exclude_impl: typing.Iterable[ImplName] = [], stream: bool = False) -> pytest.MarkDecorator:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the FnTestClassAliasInterface.

        Args:
            exclude_impl : Iterable[ImplName]
                The names of the implementations to exclude from testing.
            stream: bool
                If set, will return a streamable version of the test function.

        Usage:
            ```python
            # All implementations except the given impl will be tested.

            @baml.FnTestClassAlias.test(exclude_impl=["implname"])
            async def test_logic(FnTestClassAliasImpl: IFnTestClassAlias) -> None:
                result = await FnTestClassAliasImpl(...)
            ```

            ```python
            # Streamable version of the test function.

            @baml.FnTestClassAlias.test(stream=True)
            async def test_logic(FnTestClassAliasImpl: IFnTestClassAliasStream) -> None:
                async for result in FnTestClassAliasImpl(...):
                    ...
            ```
        """
        ...

    @typing.overload
    def test(self, test_class: typing.Type[CLS]) -> typing.Type[CLS]:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the FnTestClassAliasInterface.

        Args:
            test_class : Type[CLS]
                The test class to be decorated.

        Usage:
        ```python
        # All implementations will be tested in every test method.

        @baml.FnTestClassAlias.test
        class TestClass:
            def test_a(self, FnTestClassAliasImpl: IFnTestClassAlias) -> None:
                ...
            def test_b(self, FnTestClassAliasImpl: IFnTestClassAlias) -> None:
                ...
        ```
        """
        ...

BAMLFnTestClassAlias: IBAMLFnTestClassAlias
