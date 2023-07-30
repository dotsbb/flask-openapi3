# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2023/7/4 9:35
from typing import TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from .path_item import PathItem
else:
    PathItem = "PathItem"

"""
A map of possible out-of band callbacks related to the parent operation.
Each value in the map is a [Path Item Object](#pathItemObject)
that describes a set of requests that may be initiated by the API provider and the expected responses.
The key value used to identify the path item object is an expression, evaluated at runtime,
that identifies a URL to use for the callback operation.
"""
Callback = Dict[str, PathItem]
