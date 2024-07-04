#!/usr/bin/env python3
"""duck type an iterable object"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence])\
        -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """Get the lenght of lst"""
    return [(i, len(i)) for i in lst]
