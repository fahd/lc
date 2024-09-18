class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        o = {}
        for char in ransomNote:
            if char not in o:
                o[char] = 0
            o[char] += 1
        for char in magazine:
            if char in o:
                o[char] -= 1
                if o[char] == 0:
                    del o[char]
                if len(o) == 0:
                    return True
        return len(o) == 0