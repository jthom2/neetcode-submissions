class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = len(s)-1

        for l in range(len(s)):
            # if l == r: return False
            if not s[l].isalnum(): continue
            while not s[r].isalnum():
                r -= 1 
                

            cl = s[l].lower()
            cr = s[r].lower()

            print(cl, cr)

            if cl != cr: return False

            r -= 1
        
        return True

        