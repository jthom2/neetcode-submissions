class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pos = False; c = 0

        if len(nums) == 1:
            if nums[0] > 1: return 1
            if nums[0] < 1: return 1
            else: return 2
            
        
        for i, n in enumerate(nums):
            if (i == n-1): c+=1

            if n < 1: continue
            else: pos = True

            # n is not negative
            try:
                if (nums[n-1] != n):
                    checki = i
                    nums[n-1], nums[i] = n, nums[n-1]

                    if nums[i] < 1: 
                        tmp = nums[i]
                        nums[i] = nums[-1]
                        nums[-1] = tmp

                    try:
                        if (nums[checki]-1 > 0) and (nums[nums[checki]-1] != checki):
                            tmp = nums[nums[checki]-1]
                            nums[nums[checki]-1] = nums[checki]
                            nums[checki] = tmp
                    except: pass                    
            except: pass


        for i, n in enumerate(nums):
            if (n != i+1): return i+1
            elif (i == len(nums)-1) and (n == i+1):
                return nums[-1]+1

        return -1
        