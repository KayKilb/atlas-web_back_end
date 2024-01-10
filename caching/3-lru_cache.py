#!/usr/bin/env python3
"""
Create a class LRUCache that inherits from BaseCaching
and is a caching system
"""
from typing import Any
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Child-class implementing a pair of key/value algorithm (LRU)"""

    def __init__(self):
        """LRU Cache constructor"""
        super().__init__()
        self.keys_orders = []

        def _add_element(self, key, value):
            """adds an item to the cache while keeping track of its position in the cache order"""
            if key in self.keys_orders:
                self.keys_orders.remove(key)

            self.keys_orders.append(key)
            self.cache_data[key] = value

    def put(self, key, value):
        """Inserting value into cache"""
        if not key or not value:
            return

        if self.cache_data.get(key):
            self._add_element(key, value)
            return

        keys = list(self.cache_data.keys())
        if len(keys) == BaseCaching.MAX_ITEMS:
            """
            process that removes the least recently used (LRU)
            item from the cache when the number of items reaches
            the maximum allowed. After removal, it adds a new
            key-value pair to the cache using the LRU method
            """
            remove_key = self.keys_orders[0]
            self.keys_orders.pop(0)
            print('DISCARD: {}'.format(remove_key))
            del self.cache_data[remove_key]
            self._add_element(key, value)
            return

        self._add_element(key, value)

    def get(self, key):
        """Retrieves value from cache"""
        if not key:
            return None

        el = self.cache_data(key)
        if not el:
            return None

        # Reorder the keys level so the usage will be taken in count
        self.keys_orders.remove(key)
        self.keys_orders.append(key)
        return self.cache_data.get(key)
