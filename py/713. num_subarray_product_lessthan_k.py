class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = r = total = 0
        curr = 1

        if k == 0:
            return 0
        
        while r < len(nums):
            curr *= nums[r]

            while curr >= k and l < r:
                curr /= nums[l]
                l += 1
            
            if curr < k:
                total += (r - l + 1)
            
            r += 1
        return total
        