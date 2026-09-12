class Solution:
    def firstUniqChar(self, s: str) -> int:

        i = 0
        for c in s:
            if s.count(c) == 1: return i
            i += 1


        return -1