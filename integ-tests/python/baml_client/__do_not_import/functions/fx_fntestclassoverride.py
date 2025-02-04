# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.classes.cls_overrideclass import OverrideClass
from ..types.partial.classes.cls_overrideclass import PartialOverrideClass
from baml_core.stream import AsyncStream
from baml_lib._impl.functions import BaseBAMLFunction
from typing import AsyncIterator, Callable, Protocol, runtime_checkable


IFnTestClassOverrideOutput = OverrideClass

@runtime_checkable
class IFnTestClassOverride(Protocol):
    """
    This is the interface for a function.

    Args:
        arg: str

    Returns:
        OverrideClass
    """

    async def __call__(self, arg: str, /) -> OverrideClass:
        ...

   

@runtime_checkable
class IFnTestClassOverrideStream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        arg: str

    Returns:
        AsyncStream[OverrideClass, PartialOverrideClass]
    """

    def __call__(self, arg: str, /) -> AsyncStream[OverrideClass, PartialOverrideClass]:
        ...
class IBAMLFnTestClassOverride(BaseBAMLFunction[OverrideClass, PartialOverrideClass]):
    def __init__(self) -> None:
        super().__init__(
            "FnTestClassOverride",
            IFnTestClassOverride,
            ["v1"],
        )

    async def __call__(self, *args, **kwargs) -> OverrideClass:
        return await self.get_impl("v1").run(*args, **kwargs)
    
    def stream(self, *args, **kwargs) -> AsyncStream[OverrideClass, PartialOverrideClass]:
        res = self.get_impl("v1").stream(*args, **kwargs)
        return res

BAMLFnTestClassOverride = IBAMLFnTestClassOverride()

__all__ = [ "BAMLFnTestClassOverride" ]
