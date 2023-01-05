#!/usr/bin/env python3
"""
    Callable function annotation
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Args:
            multiplier: factor
        Return:
            multiplication in float
    """

    def x(f: float) -> float:
        """
           multiplies multiplier argument above by f
           and returns the result
        """
        return float(f * multiplier)

    return x
