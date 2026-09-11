class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        b = set(arr2)   ;   mp = {}       ; res = []



        extra = []

        
            




        for n in arr1:
            if n not in b: extra.append(n)
            elif n not in mp: mp[n] = 1; continue
            elif n in mp: mp[n] += 1; continue

        for n in arr2:
            if n in mp:
                for i in range(mp[n]): res.append(n)


        extra.sort()





        return res + extra


        