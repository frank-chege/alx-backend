#!/usr/bin/env python3
'''implements the mru caching algorithm'''

from base_caching import BaseCaching

class LRUCache(BaseCaching):
    '''implements mru caching'''
    def __init__(self):
        super().__init__()
        self.access_list = []
    
    def put(self, key, item):
        '''adds an item to the cache'''
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            #remove the mru item
            removed_key = self.access_list.pop()
            self.cache_data.pop(removed_key)
            print(f'DISCARD: {removed_key}')
    
        self.cache_data[key] = item
    
    def get(self, key):
        '''returns the value of the given key'''

        value = self.cache_data.get(key)
        if key is None or value is None:
            return None
        else:
            #add the accessed key to a list to know the most recently used
            if key in self.access_list:
                self.access_list.remove(key)
            self.access_list.append(key)
            return value
