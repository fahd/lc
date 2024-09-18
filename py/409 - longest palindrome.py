"""
even and odd
abccccdd
{
    d:2,
    c:4,
    a:1,
    b:3,
}

4 + 2 + 2
odd = +1

cccdeeefffmmmmm
{
    d:1,
    c:3,
    e:3,
    f:3,
    m:5
}
mfmecmcemfm
4 + 2 + 2 + 2
odd = +1

if even:
    add the number
if all odd:
    add the largest odd + the next largest odds (each minus - 1)
if even and odd:
    add the evens and the largest odd

"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        d = {}
        c = 0
        of = False

        for char in s:
            if char not in d:
                d[char] = 0
            d[char] += 1

        for k, v in d.items():
            if v % 2 == 0:
                c += v
            if v % 2 != 0:
                c += v - 1
                if not of:
                    of = True
        if of:
            c += 1
        
        return c

        

        