class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search_left(nums:List[int], target:int) -> int:
            s = 0
            e = len(nums) - 1
            
            while s <= e:
                m = (s + e) // 2
                mV = nums[m]

                if mV < target:
                    s = m + 1
                else:
                    e = m - 1
            return s

        def search_right(nums:List[int], target:int) -> int:
            s = 0
            e = len(nums) - 1
            
            while s <= e:
                m = (s + e) // 2
                mV = nums[m]

                if mV <= target:
                    s = m + 1
                else:
                    e = m - 1
            return e

      
        left = search_left(nums, target)
        right = search_right(nums, target)

        if not (left <= right):
            return [-1, -1]

        return [left,right]