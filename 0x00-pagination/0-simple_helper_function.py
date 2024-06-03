#!/usr/bin/env python3
'''introduction to pagination'''
from typing import Tuple

def index_range(page:int, page_size:int)->Tuple:
    '''returns start abd end index'''
    end_idx = page * page_size
    start_idx = end_idx - page_size
    return (start_idx, end_idx)