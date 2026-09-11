class Solution:
    def hammingWeight(self, n: int) -> int:
        
        binn = str(bin(n))
        t = 0
        for x in binn:
            print(x)
            if x == '1':
                t += 1

        return t