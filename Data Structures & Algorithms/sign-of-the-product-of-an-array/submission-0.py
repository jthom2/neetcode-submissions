class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(x):
            if x > 0: return 1
            if x < 0: return -1
            else: return 0
        return signFunc(math.prod(nums))