class Solution:
    def reverseBits(self, n: int) -> int:
        
        k = str(bin(n))[::-1]
        x = k[:-2]
        x = x + "0"*(32 - len(x))
        

        i = 31
        total = 0
        for c in x:
            if c == '1':
                total += pow(2, i)
            
            i -= 1
        
        return total

        
        
        
