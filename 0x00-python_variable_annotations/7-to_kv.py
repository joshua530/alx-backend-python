#!/usr/bin/env python3
"""
    Mixed tuple annotation
    Union[a,b,c] = contains a, b, or c
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        Args:
            k: String
            v: Union: Can be int or float
        Return:
            Tuple with string and int or float
    """

    concat: Tuple[str, Union[int, float]] = (k, v**2)

    return concat
