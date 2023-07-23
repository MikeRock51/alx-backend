#!/usr/bin/env python3
"""
    Implement a method named get_page that takes two integer arguments
    page with default value 1 and page_size with default value 10.

        - You have to use this CSV file (same as the one presented
            at the top of the project)
        - Use assert to verify that both arguments are integers greater than 0.
        - Use index_range to find the correct indexes to paginate the dataset
        - correctly and return the appropriate page of the dataset
            (i.e. the correct list of rows).
        - If the input arguments are out of range for the dataset, an empty
            list should be returned.
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

        print(self.dataset()[startIndex:endIndex])


Server().get_page(1, 3)
