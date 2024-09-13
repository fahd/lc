from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i,v in enumerate(nums):
            diff = target - v
            if diff in s:
                return [s[diff], i]
            s[v] = i
        return []

