class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0; r = len(heights)-1; max_storage = 0

        while l<r:
            w = r - l
            h = min(heights[r], heights[l])
            
            storage = w * h

            max_storage = max(max_storage, storage)

            if heights[l] < heights[r]: l += 1
            else: r -=1
        
        return max_storage
        