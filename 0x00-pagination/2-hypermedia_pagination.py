#!/usr/bin/env python3
"""
    Replicate code from the previous task.
    Implement a get_hyper method that takes the same arguments
    (and defaults) as get_page and returns a dictionary containing
    the following key-value pairs:
        - page_size: the length of the returned dataset page
        - page: the current page number
        - data: the dataset page (equivalent to return from previous task)
        - next_page: number of the next page, None if no next page
        - prev_page: number of the previous page, None if no previous page
        - total_pages: the total number of pages in the dataset as an integer
    Make sure to reuse get_page in your implementation.
"""

from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int]:
    """Computes and returns the start and end indexes of requested page"""
    startIndex = page_size * (page - 1)
    endIndex = startIndex + page_size

    return (startIndex, endIndex)


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
        """Performs a simple pagination"""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        startIndex, endIndex = index_range(page, page_size)

        return self.dataset()[startIndex:endIndex]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Performs a hypermedia pagination"""
        dataset = self.get_page(page, page_size)

        next_page = None
        prev_page = None
        total_pages = math.ceil(len(self.__dataset) / page_size)
        if dataset != [] and page + 1 < total_pages:
            next_page = page + 1

        if page - 1 > 0:
            prev_page = page - 1

        hyper = {
            "page_size": len(dataset),
            "page": page,
            "data": dataset,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

        return hyper
