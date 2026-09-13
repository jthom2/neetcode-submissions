class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(l):
            if sum(nums[0:i]) == sum(nums[i+1:l]): return i            
        return -1