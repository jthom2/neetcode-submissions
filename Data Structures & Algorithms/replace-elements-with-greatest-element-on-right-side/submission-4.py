class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        n = len(arr) ; res = [0] * n ; rightMax = -1


        i = n - 1
        for n in arr[::-1]:

            res[i] = rightMax
            rightMax = max(arr[i], rightMax)

            i -= 1
        
        return res

        