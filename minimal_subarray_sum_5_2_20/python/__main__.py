import typing
from typing import List

# Who doesn't love a one-liner?
def find_shortest_subarray(arr: List[int], target: int) -> int:
    """
    Provided a list of ints,
    return the length of the shortest find_shortest_subarray
    whose value is greater than the target

    If no such subarray exists, return 0
    """
    return 0 if (len(arr) == 0 or sum(arr) < target) else\
        min([end - start for start in range(len(arr)) for end in range(start+1, len(arr) + 1)
        if sum(arr[start:end]) >= target])


# For sane people
def readable_shortest_subarray(arr: List[int], target: int) -> int:
    """
    Provided a list of ints,
    return the length of the shortest find_shortest_subarray
    whose value is greater than the target

    If no such subarray exists, return 0
    """
    if len(arr) == 0 or sum(arr) < target:
        return 0
    for depth in range(1, len(arr) + 1):
        for pos in range(len(arr) - depth + 1):
            if sum(arr[pos:pos+depth]) >= target:
                return depth
    return 0
        
