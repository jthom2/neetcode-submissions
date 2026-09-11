class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums = sorted(nums)

        for i, n in enumerate(nums):
            if i != 0 and n - nums[i-1] != 1:
                return n - 1
            if i == 0 and n != 0:
                return 0
            if i == len(nums) - 1 and n != len(nums):
                return len(nums)



        return -1
   