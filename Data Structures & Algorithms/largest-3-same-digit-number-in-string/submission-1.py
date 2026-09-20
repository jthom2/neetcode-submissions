class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""

        l = 0; r = 2
        for i in range(1, len(num)-1):
            if num[l] == num[i] == num[r]:
                if ans < num[l]: ans = (num[l] * 3)
            l += 1; r += 1
        
        return ans
