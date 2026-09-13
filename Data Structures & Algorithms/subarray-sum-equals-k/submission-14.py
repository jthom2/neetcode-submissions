class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0: 1}
        l = len(nums)
        s = 0; res=0

        for i in range(l):
            s += nums[i]
            diff = s - k
            res += prefixSums.get(diff, 0)
            prefixSums[s] = 1 + prefixSums.get(s, 0)

        return res
