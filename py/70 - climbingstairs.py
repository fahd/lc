class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        ways = {1:1, 2:2}
        s = 3
        while s < n + 1:
            nV = ways[s-1] + ways[s-2]
            ways[s] = nV
            s += 1

        return ways[n]

        # INEFFICIENT
        # s = []
        # c = 0
        # s.append(n - 1)
        # s.append(n - 2)
        # while len(s):
        #     v = s.pop()
        #     if v == 0:
        #         c += 1
        #     n1 = v - 1
        #     n2 = v - 2
        #     if n1 > -1:
        #         s.append(n1)
        #     if n2 > -1:
        #         s.append(n2)
        # return c

        