#!/usr/bin/env python3
"""The types of the elements of"""

import typing


T = typing.TypeVar('T', bound=typing.Any)


def safely_get_value(
        dct: typing.Mapping,
        key: typing.Any,
        default: typing.Union[T, None] = None,
        ) -> typing.Union[typing.Any, T]:
    """Safe ly get val ue"""
    if key in dct:
        return dct[key]
    else:
        return default
