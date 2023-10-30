# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.
#
# BAML version: 0.0.1
# Generated Date: 2023-10-29 18:32:10.278897 -07:00
# Generated by: vbv

from ..types.classes.cls_type1 import Type1
from ..types.classes.cls_type2 import Type2
from typing import Protocol, runtime_checkable


import typing

import pytest

ImplName = typing.Literal[]

T = typing.TypeVar("T", bound=typing.Callable[..., typing.Any])
CLS = typing.TypeVar("CLS", bound=type)


@runtime_checkable
class IFunctionOne(Protocol):
    """
    This is the interface for a function.

    Args:
        arg: Type1

    Returns:
        Type2
    """

    async def __call__(self, arg: Type1, /) -> Type2:
        ...


class BAMLFunctionOneImpl:
    async def run(self, arg: Type1, /) -> Type2:
        ...

class IBAMLFunctionOne:
    def register_impl(
        self, name: ImplName
    ) -> typing.Callable[[IFunctionOne], IFunctionOne]:
        ...

    def get_impl(self, name: ImplName) -> BAMLFunctionOneImpl:
        ...

    @typing.overload
    def test(self, test_function: T) -> T:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the FunctionOneInterface.

        Args:
            test_function : T
                The test function to be decorated.

        Usage:
            ```python
            # All implementations will be tested.

            @baml.FunctionOne.test
            def test_logic(FunctionOneImpl: IFunctionOne) -> None:
                result = await FunctionOneImpl(...)
            ```
        """
        ...

    @typing.overload
    def test(self, *, exclude_impl: typing.Iterable[ImplName]) -> pytest.MarkDecorator:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the FunctionOneInterface.

        Args:
            exclude_impl : Iterable[ImplName]
                The names of the implementations to exclude from testing.

        Usage:
            ```python
            # All implementations except "" will be tested.

            @baml.FunctionOne.test(exclude_impl=[""])
            def test_logic(FunctionOneImpl: IFunctionOne) -> None:
                result = await FunctionOneImpl(...)
            ```
        """
        ...

    @typing.overload
    def test(self, test_class: typing.Type[CLS]) -> typing.Type[CLS]:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the FunctionOneInterface.

        Args:
            test_class : Type[CLS]
                The test class to be decorated.

        Usage:
        ```python
        # All implementations will be tested in every test method.

        @baml.FunctionOne.test
        class TestClass:
            def test_a(self, FunctionOneImpl: IFunctionOne) -> None:
                ...
            def test_b(self, FunctionOneImpl: IFunctionOne) -> None:
                ...
        ```
        """
        ...

BAMLFunctionOne: IBAMLFunctionOne
