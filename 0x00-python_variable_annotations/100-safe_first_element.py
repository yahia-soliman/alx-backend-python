#!/usr/bin/env python3
"""The types of the elements of"""

import typing


def safe_first_element(lst: typing.Sequence[typing.Any])\
        -> typing.Union[typing.Any, None]:
    """of the input are not know"""
    if lst:
        return lst[0]
    else:
        return None
