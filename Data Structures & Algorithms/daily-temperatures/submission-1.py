class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []; res = [0]*len(temperatures)

        for i, t in enumerate(temperatures):
            cur = [i, t]
            if not s or (s[-1][1] > cur[1]): 
                s.append(cur); continue
            while s and (s[-1][1] < cur[1]):
                popped = s.pop()
                res[popped[0]] = (cur[0] - popped[0])
            s.append(cur)
        return res