class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = 0


        left = 0
        right = len(heights) - 1

        volumes = []

        for i in range(len(heights)):
            
            vol = abs(right - left) * min(heights[right], heights[left])
            

            if heights[right]  < heights[left]: right -= 1
            elif heights[left] < heights[right]: left +=1
            else: left +=1

            if vol > volume: volume = vol; print(vol)


                

        

        return volume
        