#!/usr/bin/env python3
"""
a method named get_page that takes two integer arguments page with
default value 1 and page_size with default value 10
"""
import csv
import math
from typing import List, Tuple


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
        """Retrieve a specific page from the dataset."""
        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        start, end = index_range(page, page_size)
        dataset = self.dataset()
        if start >= len(dataset):
            return []

        return dataset[start:end]

    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
        return a tuple of size two containing a
        start index and an end index corresponding
        to the range of indexes to return in a list
        for those particular pagination parameters
        """
        start_index = page_size * (page - 1)
        end_index = page_size * page

        return (start_index, end_index)
