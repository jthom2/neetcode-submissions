class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = len(s)-1

        for l in range(len(s)):
            # if l == r: return False
            if not s[l].isalnum(): continue
            while not s[r].isalnum(): r -= 1 

            if s[l].lower() != s[r].lower(): return False

            r -= 1
        
        return True

        