class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sc = 0
    
        for char in t:
            if sc == len(s):
                return True

            elif char == s[sc]:
                sc+= 1
            
        return sc == len(s)
