class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        lth = len(grid)*len(grid); res = []; seen = {}

        a, b = -1, -1

        for lst in grid:
            for n in lst:
                if n in seen: a = n
                else:
                    seen[n] = 1
        for b in range(1, lth+1): 
            if b not in seen: res = [a, b]
        
        return res