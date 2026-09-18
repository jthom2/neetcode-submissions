class Solution:
    def scoreOfString(self, s: str) -> int:
        sm = 0

        if len(s) < 2: return 0

        for i, c in enumerate(s):
            if (i == 0): sm += abs(ord(s[i+1]) - ord(c))
            elif (i == len(s)-1): pass
                

            else: sm += abs(ord(s[i+1]) - ord(c))
            print(c, sm)

                
        

        return sm
        