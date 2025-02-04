# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from baml_lib._impl.deserializer import register_deserializer
from pydantic import BaseModel
from typing import Optional


@register_deserializer({  })
class DynamicPropsClass(BaseModel):
    prop1: str
    prop2: str
    prop3: int
    @property
    def display(self) -> str:
        for i in range(10):
          print(i)
        return self.prop1 + self.prop2
