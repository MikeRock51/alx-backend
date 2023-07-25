#!/usr/bin/env python3
"""
    Create a class LFUCache that inherits from BaseCaching
    and is a caching system:

    - You must use self.cache_data - dictionary from the
      parent class BaseCaching
    - You can overload def __init__(self): but don’t
      forget to call the parent init: super().__init__()
    - def put(self, key, item):
        - Must assign to the dictionary self.cache_data
          the item value for the key key.
        - If key or item is None, this method should not do anything.
        - If the number of items in self.cache_data is higher
          that BaseCaching.MAX_ITEMS:
            - you must discard the least frequency used item (LFU algorithm)
            - if you find more than 1 item to discard, you must use the LRU
              algorithm to discard only the least recently used
            - you must print DISCARD: with the key discarded and
              following by a new line
    - def get(self, key):
        - Must return the value in self.cache_data linked to key.
        - If key is None or if the key doesn’t exist
          in self.cache_data, return None.
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Defines a LFU cachning system"""
    __usage = {}

    def __init__(self):
        """Initialize an Instance"""
        super().__init__()

    def put(self, key, item):
        """Caches the given data using LFU algorithm"""
        if key and item:
            cache = self.cache_data
            if cache.get(key):
                del cache[key]
            cache[key] = item
            if len(cache) > self.MAX_ITEMS:
                minUsageValue = min(self.__usage.values())
                minUsageKeys = [k for k in self.__usage.keys()
                                if self.__usage[k] == minUsageValue]
                trash = minUsageKeys[0]
                cache.pop(trash)
                self.__usage.pop(trash)
                print('DISCARD: {}'.format(trash))
            if key in self.__usage:
                self.__usage[key] += 1
            else:
                self.__usage[key] = 0

    def get(self, key):
        """Returns the value of key from self.cache_data"""
        if not self.cache_data.get(key):
            return None

        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        self.__usage[key] += 1

        return self.cache_data[key]
