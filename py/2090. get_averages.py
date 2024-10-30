'''
[7,4,3,9,1,8,5,2,6]
        i
    l           r
            
li = 2
ri = 8

45 - 11
34 / 7

[7,11,14,23,24,32,37,39,45]
[-1, -1, -1, 5, 4, 4, -1, -1, -1]
'''

from typing import List

class Solution:
	def getAverages(self, nums: List[int], k: int) -> List[int]:
		n = len(nums)
		r = (k * 2) + 1
		avgs = []
		prefix_sum = [nums[0]]
		
		for i in range(1,len(nums)):
			prefix_sum.append(nums[i] + prefix_sum[-1])

		for i in range(len(nums)):
			l_idx = i - k
			r_idx = i + k
			
			if l_idx < 0 or r_idx >= n:
				avgs.append(-1)
			else:
				if l_idx == 0:
					avgs.append(prefix_sum[r_idx] // r)
				else:
					avgs.append((prefix_sum[r_idx] - prefix_sum[l_idx - 1]) // r)
		
		return avgs
		


		