class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = []; mp = {}

        for n in nums:
            if n not in mp: mp[n] = 1
            else: mp[n] += 1

        for i in range(-50000, 50001):
            if i not in mp: continue
            if i in mp:
                for j in range(mp[i]):
                    res.append(i)

        return res

        