#!/usr/bin/env python3
"""Basic-caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """object that allows storing and
    retrieving items from a dictionary.
    """
    def put(self, key, item):
        """Adds an item to cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves item by key.
        """
        return self.cache_data.get(key, None)
