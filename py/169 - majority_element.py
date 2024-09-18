import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        limit = math.floor(len(nums) / 2)
        nums.sort()
        curr = nums[0]
        c = 1
        maj = None

        if c > limit:
            return curr
        
        # [2,3,3]
        #    ^
        for i in range(1,len(nums)):
            v = nums[i]
            if curr != v:
                c = 0
                curr = v
            c += 1
            if c > limit:
                maj = curr
            
        return maj