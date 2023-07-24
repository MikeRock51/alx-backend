#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Perform a deletion-resillient hypermedia pagination"""
        indexedDataset = self.indexed_dataset()
        assert index < max(indexedDataset.keys())

        dataset = []

        i = index

        while len(dataset) < page_size:
            if indexedDataset.get(i):
                dataset.append(indexedDataset.get(i))
            i += 1

        hyper = {
                "index": index,
                "next_index": i,
                "page_size": len(dataset),
                "data": dataset
            }

        return hyper

# Server().get_hyper_index(3, 2)
