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
            v = s[i]
            prev = s[i+1]
            if v == 'I' and (prev == 'V' or prev == 'X'):
                c -= 1
            elif v == 'X' and (prev == 'L' or prev == 'C'):
                c -= 10
            elif v == 'C' and (prev == 'D' or prev == 'M'):
                c -= 100
            else:
                c += o[v]
            i-=1
        return c