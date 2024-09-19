class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for item in nums:
            if item not in s:
                s.add(item)
            else:
                return True
        return False