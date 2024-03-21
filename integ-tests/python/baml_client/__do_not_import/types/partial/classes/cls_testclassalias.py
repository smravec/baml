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


@register_deserializer({ "key-dash": "key","key21": "key2","key with space": "key3","key.with.punctuation/123": "key5", })
class PartialTestClassAlias(BaseModel):
    key: Optional[str] = None
    key2: Optional[str] = None
    key3: Optional[str] = None
    key4: Optional[str] = None
    key5: Optional[str] = None