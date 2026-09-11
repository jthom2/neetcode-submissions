class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        triplets, diffs = [], {}



        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]: continue

            l, r = (i + 1), (len(nums) - 1)

            while l < r:
                threeSum = n + nums[l] + nums[r]

                if   threeSum > 0:   r -= 1
                elif threeSum < 0:   l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res









        # for i, n in enumerate(nums):
            
        #     target = n * (-1)


        #     for j, m in enumerate(nums):
        #         if j == 0 and i == 0: continue



        #         else:
                

        #             tget = target - m
        #             diffs[m] = j

        #             if tget in diffs:
        #                 if (diffs[tget] != i) and (diffs[tget] != j) and (i != j):
        #                     tmp = sorted([n, m, tget])
        #                     if tmp not in triplets:
        #                         triplets.append(tmp)

        #                 elif (n == 0) and (n == 0) and (m == 0) and nums.count(0) > 2:
        #                     tmp = sorted([n, m, tget])
        #                     if tmp not in triplets:
        #                         triplets.append(tmp)
            
            

        

        # return triplets
