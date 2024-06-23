#!/usr/bin/env python3
"""A module that defines a helper function."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns the starting and ending index of pages.

    Args:
        page: The number of the page.
        page_size: The size of the page.

    Returns:
        A tuple of start and end indexes for the requested page number.
    """
    start_index = 0
    if (page != 1):
        start_index = (page - 1) * page_size

    end_index = page * page_size

    return ((start_index, end_index))
