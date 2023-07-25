#!/usr/bin/env python3
"""
    Create a class BasicCache that inherits from BaseCaching
    and is a caching system:
        - You must use self.cache_data - dictionary from the parent
          class BaseCaching
        - This caching system doesn’t have limit
        - def put(self, key, item):
            - Must assign to the dictionary self.cache_data the item
              value for the key key.
            - If key or item is None, this method should not do anything.
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A basic caching system"""
    def __init__(self):
        """Initializes an Instance"""
        super().__init__()

    def put(self, key, item):
        """Assigns the key, value to self.cache_data"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value of key from self.cache_data"""
        if not self.cache_data.get(key):
            return None
        return self.cache_data[key]


if __name__ == "__main__":
    cache = BasicCache()
    cache.put('Name', 'Mike Rock')
    print(cache.get('Name'))
