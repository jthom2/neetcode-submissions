class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        count = Counter(nums)

        i = 1
        while True:
            if i not in count: return i
            i += 1