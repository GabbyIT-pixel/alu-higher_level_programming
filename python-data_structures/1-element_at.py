#!/usr/bin/python3
"""
Return element at a given index like in C.
"""


def element_at(my_list, idx):
    """Retrieve element at index `idx` from `my_list`.

    Returns None when idx is negative or out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
