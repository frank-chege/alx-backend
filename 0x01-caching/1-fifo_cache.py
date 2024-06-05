#!/usr/bin/env python3
'''implements the fifo caching algorithm'''

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    '''implements fifo caching'''
    def __init__(self):
        super().__init__()
    
    def put(self, key, item):
        '''adds an item to the cache'''
        if key is None or item is None:
            return
        if len(self.cache_data) > self.MAX_ITEMS:
            #remove the first item
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print(f'DISCARD: {first_key}')
        else:
            self.cache_data[key] = item
    
    def get(self, key):
        '''returns the value of the given key'''
        value = self.cache_data.get(key)
        if key is None or value is None:
            return None
        else:
            return value