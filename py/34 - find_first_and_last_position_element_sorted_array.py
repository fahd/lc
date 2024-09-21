class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        minV = None
        maxV = None
        l = 0
        r = len(nums) - 1
        lb = None
        rb = None
        m_found = -1
        default = [-1, -1]

        # find m == t
        while l <= r:
            m = (l + r) // 2
            mV = nums[m]
            if mV == target:
                lb, rb = l, r
                m_found = m
                break
            # go right
            elif mV < target: 
                l = m + 1
            # go left
            else:    
                r = m - 1

        if m_found < 0:
            return default
        
        l_local = lb
        r_local = rb


        # go left
        l_left = l_local
        r_left = m_found

        
        while l_left <= r_left:
            m_left = (l_left + r_left) // 2
            mlv = nums[m_left]
            if mlv == target and m_left == 0:
                minV = m_left
                break
            elif mlv == target and nums[m_left - 1] != target:
                minV = m_left
                break
            elif mlv < target:
                l_left = m_left + 1
            elif mlv > target:
                r_left = m_left - 1
            else:
                r_left -= 1

        # go right
        l_right = m_found
        r_right = r_local
        
        while l_right <= r_right:
            m_right = (l_right + r_right) // 2
            mrv = nums[m_right]
            if mrv == target and m_right == len(nums) - 1:
                maxV = m_right
                break
            elif mrv == target and nums[m_right + 1] != target:
                maxV = m_right
                break
            elif mrv < target:
                l_right = m_right + 1
            elif mrv > target:
                r_right = m_right - 1
            else:
                l_right += 1
        
        return [minV, maxV]
    # print('minV', minV)