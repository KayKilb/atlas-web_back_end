#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits from BaseCaching
and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Child-class implementing a pair of key/value algorithm (FIFO)"""

    def put(self, key, value):
        """Inserting value into cache"""
        if not key or not value:
            return

        keys = self.cache_data.keys()
        if len(keys) == BaseCaching.MAX_ITEMS:
            temp_key = list(keys)[0]
            del self.cache_data[temp_key]
            print('DISCARD: {}'.format(temp_key))

        self.cache_data[key] = value

    def get(self, key):
        """Retrieves value from cache"""
        if not key:
            return None

        return self.cache_data.get(key)
