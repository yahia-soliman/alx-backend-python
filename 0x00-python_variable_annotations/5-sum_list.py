#!/usr/bin/env python3
"""Complex types - list of floats"""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """Get the sum of a list of floats"""
    sum: float = 0
    for n in input_list:
        sum += n
    return sum
