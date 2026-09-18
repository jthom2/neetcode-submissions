class Solution:
    def findLucky(self, arr: List[int]) -> int:
        luckies = [-1]; counts = Counter(arr)
        
        for n in arr:
            if counts[n] == n: luckies.append(n)

        return max(luckies)
        