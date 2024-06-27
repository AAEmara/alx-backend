#!/usr/bin/env python3
"""A module that defines an MRU Cache Class."""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A Class that uses the Most Recently Used (MRU) Policy.
    """
    mru_dict = dict()
    mru_key = None
    mru_id = -1

    def __init__(self):
        """Initializing the LRUCache with parent's attributes.
        """
        super().__init__()

    def put(self, key, item):
        """Manages the insertion new data in the Cache Memory using MRU.

        Note:
            The method add the item if there is an available space in the
            memory corresponding to recency ID, but it removes the highest
            ID (most recently used ID) once there is not enough space.
        """
        data = self.cache_data

        if (key is not None and item is not None):
            self.mru_id += 1
            self.mru_key = key
            data[key] = item  # Adding new item to cache.
            self.mru_dict[self.mru_key] = self.mru_id   # Updating Recency.
            item_count = len(data)
            if (item_count > BaseCaching.MAX_ITEMS):
                ids = [v for k, v in self.mru_dict.items()]
                discarded_id = sorted(ids)[-2]
                for k, v in self.mru_dict.items():
                    if (v == discarded_id):
                        discarded_key = k
                        break
                del data[discarded_key]  # Del. most recent item in cache.
                del self.mru_dict[discarded_key]  # Removing most used item.
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """Retrieves the cached data from memory according to a certain key.
        """
        try:
            data = self.cache_data[key] if (key is not None) else None
            self.mru_id += 1
            self.mru_key = key
            self.mru_dict[self.mru_key] = self.mru_id
            return data
        except KeyError:
            return (None)
