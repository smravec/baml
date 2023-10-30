# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.
#
# BAML version: 0.0.1
# Generated Date: 2023-10-29 18:32:10.278897 -07:00
# Generated by: vbv

from ..types.classes.cls_type1 import Type1
from typing import Protocol, runtime_checkable


import typing

import pytest

ImplName = typing.Literal[]

T = typing.TypeVar("T", bound=typing.Callable[..., typing.Any])
CLS = typing.TypeVar("CLS", bound=type)


@runtime_checkable
class IFunctionTwo(Protocol):
    """
    This is the interface for a function.

    Args:
        arg: Type1

    Returns:
        str
    """

    async def __call__(self, arg: Type1, /) -> str:
        ...


class BAMLFunctionTwoImpl:
    async def run(self, arg: Type1, /) -> str:
        ...

class IBAMLFunctionTwo:
    def register_impl(
        self, name: ImplName
    ) -> typing.Callable[[IFunctionTwo], IFunctionTwo]:
        ...

    def get_impl(self, name: ImplName) -> BAMLFunctionTwoImpl:
        ...

    @typing.overload
    def test(self, test_function: T) -> T:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the FunctionTwoInterface.

        Args:
            test_function : T
                The test function to be decorated.

        Usage:
            ```python
            # All implementations will be tested.

            @baml.FunctionTwo.test
            def test_logic(FunctionTwoImpl: IFunctionTwo) -> None:
                result = await FunctionTwoImpl(...)
            ```
        """
        ...

    @typing.overload
    def test(self, *, exclude_impl: typing.Iterable[ImplName]) -> pytest.MarkDecorator:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the FunctionTwoInterface.

        Args:
            exclude_impl : Iterable[ImplName]
                The names of the implementations to exclude from testing.

        Usage:
            ```python
            # All implementations except "" will be tested.

            @baml.FunctionTwo.test(exclude_impl=[""])
            def test_logic(FunctionTwoImpl: IFunctionTwo) -> None:
                result = await FunctionTwoImpl(...)
            ```
        """
        ...

    @typing.overload
    def test(self, test_class: typing.Type[CLS]) -> typing.Type[CLS]:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the FunctionTwoInterface.

        Args:
            test_class : Type[CLS]
                The test class to be decorated.

        Usage:
        ```python
        # All implementations will be tested in every test method.

        @baml.FunctionTwo.test
        class TestClass:
            def test_a(self, FunctionTwoImpl: IFunctionTwo) -> None:
                ...
            def test_b(self, FunctionTwoImpl: IFunctionTwo) -> None:
                ...
        ```
        """
        ...

BAMLFunctionTwo: IBAMLFunctionTwo
