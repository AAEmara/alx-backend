#!/usr/bin/env python3
"""A module that defines a FIFO caching policy class."""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A First In First Out cache policy class.
    """

    def __init__(self):
        """Initializing the FIFOCache class with parent's attribute.
        """
        super().__init__()

    def put(self, key, item):
        """Manages the insertion new data in the Cache Memory using FIFO.

        Note:
            The method add the item if there is an available space in the
            memory, but it removes it once there is not enough space.
        """
        if (key is not None and item is not None):
            self.cache_data[key] = item

        item_count = len(list(self.cache_data))
        if (item_count > BaseCaching.MAX_ITEMS):
            # discarded_key = self.cache_data.pop(key, None)
            key = list(self.cache_data)[0]
            del self.cache_data[key]
            print(f"DISCARD: {key}")

    def get(self, key):
        """Retrieves the cached data from memory according to a certain key.
        """
        try:
            data = self.cache_data[key] if (key is not None) else None
            return data
        except KeyError:
            return (None)
