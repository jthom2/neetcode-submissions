class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums)
        res = []

        return [item[0] for item in counts.most_common(k)]
            

            
            

        

   


        # res = []
        # nums.sort()

    


        # if           k == 1 and len(nums) == 1:    return [nums[-1]]
        # elif k == len(nums):
        #     pass


        # mp = {}

        # for i, n in enumerate(nums):
        #     if   n not in mp:   mp[n] = 1
        #     elif n     in mp:   mp[n] += 1
        


        # asc = {k: v for k, v in sorted(mp.items(), key=lambda item: item[1])}

        

        # t = list(asc.keys())

        

        

        # x = k
        # while x != 0:
        #     res.append(t[-x])
        #     x -= 1
        
        # print(res)
            
        

        
        # return res