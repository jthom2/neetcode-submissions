class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights); c = 0

        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]: c += 1

        return c