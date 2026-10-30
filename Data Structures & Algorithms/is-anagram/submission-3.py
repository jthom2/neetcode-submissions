class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        s_count = Counter(s)
        t_count = Counter(t)

        for chr in s:
            if s_count[chr] != t_count[chr]: return False

        return True
       
        