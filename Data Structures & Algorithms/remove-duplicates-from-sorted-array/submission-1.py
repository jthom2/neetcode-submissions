class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            while nums.count(n) > 1: nums.remove(n)
        return len(nums)