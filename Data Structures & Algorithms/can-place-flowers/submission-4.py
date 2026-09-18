class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        p = 0
        if len(flowerbed) == 1 and flowerbed[0] == 0: return True 

        for i, f in enumerate(flowerbed):
            if (i == 0) and (i < len(flowerbed)-1):
                if (f == 0) and (flowerbed[i+1] == 0): 
                    p += 1
                    flowerbed[i] = 1
                    print(1, i)
            elif (i == len(flowerbed)-1) and (i > 0):
                if flowerbed[i-1] == 0 and f == 0: 
                    p +=1
                    flowerbed[i] = 1
                    print(2, i)
            elif (i > 0) and (i < len(flowerbed)-1):
                if flowerbed[i-1] == 0 and f == 0 and flowerbed[i+1] == 0:
                    p +=1
                    flowerbed[i] = 1
                    print(3, i) 
           
                        

        return (p >= n)