#!/usr/bin/env python3
"""
Create a class BasicCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Child-class implementing key/value algorithm"""

    def put(self, key, value):
        """Inserting value into cache"""
        if key is None or value is None:
            return

        self.cache_data[key] = value

    def get(self, key):
        """Retrieves value from cache"""
        if not key:
            return None
        
        return self.cache_data.get(key)
