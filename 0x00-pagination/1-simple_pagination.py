#!/usr/bin/env python3
'''introduction to pagination'''
from typing import Tuple, List
import csv
import math

def index_range(page:int, page_size:int)->Tuple:
    '''returns start abd end index'''
    end_idx = page * page_size
    start_idx = end_idx - page_size
    return (start_idx, end_idx)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''return a page based on the page no. and page size given'''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        idx = index_range(page, page_size)
        start_idx = idx[0]
        end_idx = idx[1]
        if end_idx > 19419:
            return []
        self.dataset()
        return self.__dataset[start_idx:end_idx]
        
