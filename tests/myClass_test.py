import pytest
from src.myClass import total

def test_total_empty() -> None:
    """Total of empty list should be 0.0"""
    assert total([]) == 0.0

def test_total_singleItem() -> None:
    assert total([110.0]) == 110.0

def test_total_multipleItems() -> None:
    assert total([1.0, 2.0, 3.0]) == 6.0