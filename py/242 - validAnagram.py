class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map = {}

        for char in s:
            if char not in map:
                map[char] = 0
            map[char] += 1
        
        for char in t:
            if char in map:
                map[char]-= 1
                if map[char] == 0:
                    del map[char]
        return not map
    
