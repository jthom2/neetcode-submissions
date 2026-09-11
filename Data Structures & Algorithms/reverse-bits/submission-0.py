class Solution:
    def reverseBits(self, n: int) -> int:
        
        


        k = str(bin(n))
        l = k[::-1]
        x = l[:-2]
        diff = 32 - len(x)
        x = x + "0"*diff
        
        print(x)

        i = 31
        total = 0
        for c in x:
            if c == '1':
                total += pow(2, i)
            
            i -= 1
        
        return total

        
        
        
