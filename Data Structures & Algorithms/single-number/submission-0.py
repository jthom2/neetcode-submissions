class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)

        for n in nums:
            if count[n] == 1: return n
        