#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """set the key `k` with the numirec value `v`"""
    return (k, v * v)
