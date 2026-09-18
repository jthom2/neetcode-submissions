class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        p = 0
        if len(flowerbed) == 1 and flowerbed[0] == 0: return True 

        for i, f in enumerate(flowerbed):
            if (i == 0) and (i < len(flowerbed)-1):
                if (f == 0) and (flowerbed[i+1] == 0): 
                    p += 1; flowerbed[i] = 1
                    
            elif (i == len(flowerbed)-1) and (i > 0):
                if flowerbed[i-1] == 0 and f == 0: 
                    p +=1; flowerbed[i] = 1

            elif (i > 0) and (i < len(flowerbed)-1):
                if flowerbed[i-1] == 0 and f == 0 and flowerbed[i+1] == 0:
                    p +=1; flowerbed[i] = 1

        return (p >= n)