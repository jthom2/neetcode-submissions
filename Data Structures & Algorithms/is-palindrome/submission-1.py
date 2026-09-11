class Solution:
    def isPalindrome(self, s: str) -> bool:

        
        o = []
        p = ""
        for c in s:
            if (c.isalpha() or c.isnumeric()):
                o.append(c)
        
        p = "".join(o).lower()

        if p == p[::-1]:
            return True



        return False