#!/usr/bin/env python3
'''implements the fifo caching algorithm'''

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    '''implements lifo caching'''
    def __init__(self):
        super().__init__()
    
    def put(self, key, item):
        '''adds an item to the cache'''
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            #remove the last item
            
            key, value = self.cache_data.popitem()
            print(f'DISCARD: {key}')
    
        self.cache_data[key] = item
    
    def get(self, key):
        '''returns the value of the given key'''
        value = self.cache_data.get(key)
        if key is None or value is None:
            return None
        else:
            return value
