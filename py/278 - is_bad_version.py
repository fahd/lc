class Solution:
    def firstBadVersion(self, n: int) -> int:
        s, e = 1, n

        while s <= e:
            m = (s + e) // 2
            if isBadVersion(m):
                e = m - 1
            else:
                s = m + 1
        return s
