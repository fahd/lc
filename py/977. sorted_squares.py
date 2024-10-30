class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        l, r = 0, n - 1
        i = n - 1

        while l <= r:
            lV = abs(nums[l])
            rV = abs(nums[r])

            if lV > rV:
                result[i] = lV ** 2
                i -= 1
                l += 1
            else:
                result[i] = rV ** 2
                i -= 1
                r -= 1
            
        return result