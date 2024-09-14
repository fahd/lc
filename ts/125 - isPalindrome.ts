import re

def isPalindrome(s: str) -> bool:
        if len(s) == 1:
            return True
        c = re.sub(r'\W+|_', '', s.lower())

        print('c',c)

        l = 0
        r = len(c) - 1

        while l < r:
            lc = c[l]
            rc = c[r]

            if (lc != rc):
              return False
            l+=1
            r-=1
        return True

print(isPalindrome('ab_a'))