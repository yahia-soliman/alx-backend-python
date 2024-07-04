#!/usr/bin/env python3
"""Complex types - functions from functions"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Get a function that multiply by a give multiplyer"""
    def fun(n: float) -> float:
        """Multiply n by multiplyer"""
        return n * multiplier
    return fun
