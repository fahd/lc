from typing import List
    """
    two_sum problem
    """

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    two_sum solution
    """
    s = {}
    for i,v in enumerate(nums):
        diff = target - v
        if diff in s:
            return [s[diff], i]
        s[v] = i
    return []

