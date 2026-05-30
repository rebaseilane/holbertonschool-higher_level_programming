#!/usr/bin/env python3
"""Module containing CountedIterator."""


class CountedIterator:
    """Iterator that counts iterations."""

    def __init__(self, iterable):
        """Initialize iterator."""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return iterator object."""
        return self

    def __next__(self):
        """Return next item and increment count."""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return count."""
        return self.count
