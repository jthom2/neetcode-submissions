class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s); a1 = -1; a2 = 101
        
        for c in counts:
            f = counts[c]
            if (f % 2 == 0) and (f < a2): a2 = f
            elif (f % 2 != 0) and (a1 < f): a1 = f
        return a1-a2