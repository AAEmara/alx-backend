#!/usr/bin/env python3
"""A module that defines BasicCache Class."""

from base_caching import BaseCaching
import math


class BasicCache(BaseCaching):
    """A basic cache memory class.
    """

    def __init__(self):
        """Initializing the BasicCache Class.
        """
        super().__init__()
        self.MAX_ITEMS = math.inf

    def put(self, key, item):
        """Adds data to the cache memory.
        """
        if (key is not None or item is not None):
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves the cached data from memory according to a certain key.
        """
        try:
            data = self.cache_data[key] if (key is not None) else None
            return data
        except KeyError:
            return (None)
