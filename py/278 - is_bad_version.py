# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

import math

class Solution:
    def firstBadVersion(self, n: int) -> int:
        s = 1
        e = n

        while s <= e:
            m = math.floor((s + e) / 2)
            is_bad = isBadVersion(m)

            if isBadVersion(())

            print('m',m)
            print('is_bad', is_bad)

            if is_bad:
                if bad_idx < 0:
                    bad_idx = m
                else:
                    bad_idx = min(bad_idx, m)
                e = m - 1
            else:
                s = m + 1
            
        return bad_idx
                
            

            
        