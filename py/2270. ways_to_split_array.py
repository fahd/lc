class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count = 0
        prefix_sum = [nums[0]]        
        
        for i in range(1,len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[i-1])
        
        for i in range(len(prefix_sum) - 1):
            n = len(nums) - 1
            diff = prefix_sum[n] - prefix_sum[i]
            if prefix_sum[i] >= diff:
                print(prefix_sum[i], diff)
                count += 1
        
        return count
        