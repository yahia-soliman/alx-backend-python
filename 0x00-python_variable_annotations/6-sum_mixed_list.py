#!/usr/bin/env python3
"""Complex types - mixed list"""
import typing


def sum_mixed_list(mxd_list: typing.List[typing.Union[float, int]]) -> float:
    """Get the sum of a list of floats"""
    sum: float = 0
    for n in mxd_list:
        sum += n
    return sum
