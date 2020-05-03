import pytest
from . import find_shortest_subarray, readable_shortest_subarray

outcomes = (
    ([2, 3, 1, 2, 4, 3], 7, 2),
    ([], 1, 0),
    ([1, 2, 3, 4], 11, 0),
    ([4, 3, 1, 2, 8], 10, 2)
)

def test_find():
    for nums, goal, expected in outcomes:
        try:
            assert (actual := find_shortest_subarray(nums, goal)) == expected
        except AssertionError:
            print(f'For the provided {nums} with a target of {goal},\
                the expected value was {expected} but received {actual}')

def test_readable():
    for nums, goal, expected in outcomes:
        try:
            assert (actual := find_shortest_subarray(nums, goal)) == expected
        except AssertionError:
            print(f'For the provided {nums} with a target of {goal},\
                the expected value was {expected} but received {actual}')