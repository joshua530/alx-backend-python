#!/usr/bin/env python3
"""
    Duck typing and iteration
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence])\
        -> List[Tuple[Sequence, int]]:
    """
        Args:
            lst: Sequence of lists

        Return:
            List of tuple of sequence of integers
    """

    return [(i, len(i)) for i in lst]
