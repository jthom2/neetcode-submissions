class Solution:
    def isPalindrome(self, s: str) -> bool:

        
        o = []
        p = ""
        i = 0
        print(p)
        for c in s:
            if (c.isalpha() or c.isnumeric()):
                o.append(c)
            i += 1
        
        p = "".join(o)
        print(p)

        if p.lower() == p[::-1].lower():
            return True



        return False