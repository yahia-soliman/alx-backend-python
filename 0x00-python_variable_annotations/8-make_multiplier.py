#!/usr/bin/env python3
"""Complex types - functions from funcitons"""
import typing


def make_multiplier(multiplyer: float) -> typing.Callable[[float], float]:
    """Get a function that multiply by a give multiplyer"""
    def fun(n: float) -> float:
        """Multiply n by multiplyer"""
        return n * multiplyer
    return fun
