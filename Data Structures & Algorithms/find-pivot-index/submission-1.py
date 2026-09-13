class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pi = -1; lth = len(nums)

        l = 0
        r = lth-1

        for i in range(lth):
            if sum(nums[0:i]) == sum(nums[i+1:lth]): return i
            

        return -1