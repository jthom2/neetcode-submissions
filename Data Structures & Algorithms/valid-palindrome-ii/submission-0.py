class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(a: str) -> bool:
            if a == a[::-1]: return True
            else: return False
        
        wrds = [s]

        for i, c in enumerate(s):
            if i == 0:
                wrds.append(s[i+1:])
            elif i == len(s)-1:
                wrds.append(s[0:len(s)-1])
            else:
                tmp = s[0:i]
                tmp2 = s[i+1:len(s)]

                wrds.append(s[0:i] + s[i+1:len(s)])
        
        print(wrds)
                
        for wrd in wrds:
            if isPalindrome(a=wrd): return True

        return False