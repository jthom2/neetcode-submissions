class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip(); l = len(s)-1; count = 0

        while s[l] != ' ':
            count += 1; l -= 1 
            if l == -1: return count
            
        return count