class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr); dist = 0

        for s in arr:
            if counts[s] == 1:
                dist += 1
                if dist == k: return s
            
        return ""