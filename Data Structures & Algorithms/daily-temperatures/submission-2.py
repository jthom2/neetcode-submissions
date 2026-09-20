class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []; res = [0]*len(temperatures)

        for i, t in enumerate(temperatures):
            cur = [i, t]
            while s and (s[-1][1] < cur[1]):
                popped = s.pop()
                res[popped[0]] = (cur[0] - popped[0])
            s.append(cur)
        return res