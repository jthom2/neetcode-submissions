class Solution:
    def firstUniqChar(self, s: str) -> int:

        t = list(s)

        for i, c in enumerate(s):
            if s.count(c) == 1: return i

        


        return -1