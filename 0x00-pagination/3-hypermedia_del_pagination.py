#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Hypermedia information with indexes.

        Args:
            index: The index to search for.
            page_size: The max. number of indexes per page.

        Returns:
            Hypermedia Data.
        """
        indexed_dataset = self.indexed_dataset()
        indexes = list(indexed_dataset)
        # print(index)

        assert (index is not None), "Index must be a positive number."
        assert (index >= 0), "Index must be a positive number."
        assert (page_size >= 0), "Page Size must be a positive number."
        assert (index <= len(indexes)), "Index not in range."
        assert isinstance(index, int), "Values must be of an integer type."
        assert isinstance(page_size, int), "Values must be of an integer type."

        current_page = math.ceil(index / page_size)
        first_index = (page_size * (current_page - 1))  # Last Index in page.
        last_index = ((current_page * page_size) - 1)  # First Index in page.
        indexes_range = range(last_index)

        count = 0
        j = indexes[index]
        current_index = j
        data = list()

        for i in indexes[index:]:
            if (count < page_size):
                data.append(indexed_dataset[indexes[index + count]])
                count += 1
        current_index = indexes[index + count]
        hypermedia_data = {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": current_index,
        }

        return (hypermedia_data)
