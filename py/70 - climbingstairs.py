class Solution:
    def climbStairs(self, n: int) -> int:
        o = [0] * (n + 1)
        o[0] = 1
        o[1] = 1

        for i in range(2, n + 1):
            o[i] = o[i-1] + o[i-2]
        
        return o[n]