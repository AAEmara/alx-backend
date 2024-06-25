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

        assert (index is not None), "Index must be a positive number."
        assert (index >= 0), "Index must be a positive number."
        assert (page_size >= 0), "Page Size must be a positive number."
        assert (index <= len(indexes)), "Index not in range."
        assert isinstance(index, int), "Values must be of an integer type."
        assert isinstance(page_size, int), "Values must be of an integer type."

        count = 0
        data = list()
        for i, value in indexed_dataset.items():
            if (i >= index and count < page_size):
                data.append(value)
                count += 1
                continue
            if (count == page_size):
                current_index = i
                break

        hypermedia_data = {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": current_index,
        }

        return (hypermedia_data)
