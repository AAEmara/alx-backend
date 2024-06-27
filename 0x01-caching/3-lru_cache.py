#!/usr/bin/env python3
"""A module that defines an LRU Cache Class."""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A Class that uses the Least Recently Used (LRU) Policy.
    """
    lru_dict = dict()
    lru_key = None
    lru_id = -1

    def __init__(self):
        """Initializing the LRUCache with parent's attributes.
        """
        super().__init__()

    def put(self, key, item):
        """Manages the insertion new data in the Cache Memory using LRU.

        Note:
            The method add the item if there is an available space in the
            memory corresponding to recency ID, but it removes the lowest
            ID (least recently used ID) once there is not enough space.

        Example:
            {}
            lru_key = 0

            added_key = "A"
            { "0": "A" }
            lru_key = 0

            ...

            lru_keys = { "0": "A", "1": "B", "2": "C", "3": "D" }
            lru_key = 0

            added_key = "E"
            if (MAX_ITEMS == len(list(keys))):
                delete cache_data[str(lru_key)]
                lru_key += 1
            lru_keys = { "4": "E", "1": "B", "2": "C", "3": "D" }
            lru_key = 1

            added_key = "F"
            lru_keys = { "4": "E", "5": "F", "2": "C", "3": "D" }
            lru_key = 2

            added_key = "D"
            lru_keys = { "4": "E", "5": "F", "2": "C", "3": "D" }
            lru_key = 2


        """
        data = self.cache_data

        if (key is not None and item is not None):
            self.lru_id += 1
            self.lru_key = key
            self.lru_dict[self.lru_key] = self.lru_id   # Updating Recency.
            data[key] = item  # Adding new item to cache.
            item_count = len(data)
            if (item_count > BaseCaching.MAX_ITEMS):
                ids = [v for k, v in self.lru_dict.items()]
                discarded_id = min(ids)
                for k, v in self.lru_dict.items():
                    if (v == discarded_id):
                        discarded_key = k
                        break
                del data[discarded_key]  # Del. last item in cache.
                del self.lru_dict[discarded_key]  # Removing least used item.
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """Retrieves the cached data from memory according to a certain key.
        """
        try:
            data = self.cache_data[key] if (key is not None) else None
            self.lru_id += 1
            self.lru_key = key
            self.lru_dict[self.lru_key] = self.lru_id
            return data
        except KeyError:
            return (None)
