class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        

        s = []; l = [-1] * n
        for i in range(n):
            while s and heights[s[-1]] >= heights[i]: s.pop()
            if s:
                l[i] = s[-1]
            s.append(i)

        s = []; r = [n]*n
        for i in range(n-1,-1,-1):
            while s and heights[s[-1]] >= heights[i]: s.pop()
            if s:
                r[i] = s[-1]
            s.append(i)
        
        max_area = 0
        for i in range(n):
            l[i] += 1; r[i] -= 1
            a = heights[i] * (r[i]-l[i]+1)
            max_area = max(max_area, a)

        return max_area