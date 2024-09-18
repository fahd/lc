class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        c = 0

        for i in range(0, len(nums)):
            v = nums[i]
            if c == 0:
                candidate = v
            c += 1 if candidate == v else -1
        
        return candidate