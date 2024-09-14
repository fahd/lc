import math
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1

        while s <= e:
            m = math.floor((s + e) / 2)
            mid = nums[m]

            if mid == target:
                return m
            elif mid < target:
                s = m + 1
            else:
                e = m - 1
        
        return -1

 