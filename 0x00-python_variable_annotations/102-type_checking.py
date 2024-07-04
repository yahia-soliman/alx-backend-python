#!/usr/bin/env python3
"""The types of the elements of"""

import typing


def zoom_array(lst: typing.Tuple, factor: int = 2) -> typing.List:
    """Zoom an array! or Tuple"""
    zoomed_in: typing.List = [item * factor for item in lst]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
