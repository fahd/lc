class Solution:
    def romanToInt(self, s: str) -> int:
        o = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000            
        }
        i = len(s) - 2
        c = o[s[-1]]
        while i > -1:
            cV = o[s[i]]
            nV = o[s[i+1]]
            if cV < nV:
                c -= cV
            else:
                c += cV
            i -= 1
        return c