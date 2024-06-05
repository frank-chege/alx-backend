#!/usr/bin/env python3
'''base caching'''

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    '''inherits from from basecaching class'''
    def __init__(self):
        '''initialize base class'''
        super().__init__()
    
    def put(self, key, item):
        '''adds an item to the dict'''
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
    
    def get(self, key):
        '''returns the value of the given key'''
        value = self.cache_data.get(key)
        if key is None or value is None:
            return None
        else:
            return value