#!/usr/bin/env python3
"""A module that defines:
    Server (Class),
    index_range (Function)
"""

import csv
import math
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the desired page data.

        Args:
            page: The number of the page.
            page_size: The size of the page.

        Returns:
            A list that contains a list of data.
        """
        assert isinstance(page, int), "Value must be an an integer."
        assert isinstance(page_size, int), "Value must be an integer."

        if (page <= 0 or page_size <= 0):
            assert page == 0, "Value must be an integer bigger than 0."
            assert page_size == 0, "Value must be an integer bigger than 0."
            assert page < 0, "Value must be a positive integer."
            assert page_size < 0, "Value must be a positive integer."

        page_indexes = index_range(page, page_size)
        start_index = page_indexes[0]
        end_index = page_indexes[1]
        dataset = self.dataset()

        if ((end_index > len(dataset)) or (start_index > len(dataset))):
            return ([])

        return (dataset[start_index: end_index])

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """Delivering hypermedia information about the data.
        Args:
            page: The number of the page.
            page_size: The size of the page.

        Returns:
            A dictionary of the hypermedia information.
        """
        hypermedia_data = dict()
        dataset = self.get_page(page, page_size)
        dataset_size = len(self.__dataset)
        page_indexes = index_range(page, page_size)
        start_index = page_indexes[0]
        end_index = page_indexes[1]
        total_pages = math.ceil(dataset_size / page_size)

        if (page != 1 and page >= total_pages):
            prev_page = page - 1
            next_page = None
        elif (page == 1 and page >= total_pages):
            prev_page = None
            next_page = None
        elif (page == 1 and page < total_pages):
            prev_page = None
            next_page = page + 1
        else:
            prev_page = page - 1
            next_page = page + 1

        hypermedia_data = {
            "page_size": 0,
            "page": page,
            "data": dataset,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages}

        # Page Size is determined based on the start and end index compared
        # to the dataset size.
        # if (((end_index > dataset_size) or (start_index > dataset_size))):
        size_diff = dataset_size - (page * page_size)
        if (size_diff <= 0):
            hypermedia_data["page_size"] = 0  # Not a page.
        elif (size_diff > page_size):
            hypermedia_data["page_size"] = page_size  # Full page.
        else:
            hypermedia_data["page_size"] = size_diff  # Part of the page.

        return (hypermedia_data)


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
