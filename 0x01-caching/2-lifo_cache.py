#!/usr/bin/env python3
"""A module that defines a LIFO caching class."""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A Last In First Out cache policy class.
    """
    lifo_keys = list()

    def __init__(self):
        """Initializing the LIFOCache class with parent's attribute.
        """
        super().__init__()

    def put(self, key, item):
        """Manages the insertion new data in the Cache Memory using LIFO.

        Note:
            The method add the item if there is an available space in the
            memory, but it removes it once there is not enough space.
        """
        if (key in self.lifo_keys):
            self.last_key = key
        elif (len(self.lifo_keys) > 0):
            self.last_key = list(self.cache_data)[-1]

        if (key is not None and item is not None):
            self.cache_data[key] = item  # Adding new item.
            item_count = len(self.cache_data)
            if (item_count > BaseCaching.MAX_ITEMS):
                discarded_key = self.lifo_keys.pop()
                del self.cache_data[discarded_key]  # Removing last item.
                print(f"DISCARD: {discarded_key}")
        self.lifo_keys.append(key)

    def get(self, key):
        """Retrieves the cached data from memory according to a certain key.
        """
        try:
            data = self.cache_data[key] if (key is not None) else None
            return data
        except KeyError:
            return (None)
