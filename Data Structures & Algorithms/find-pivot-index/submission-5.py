class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lth = len(nums); prefixSum = {}; sm = 0; postfixSum = {}; pm = 0; j = lth-1

        for i in range(lth):
            sm += nums[i]; prefixSum[i] = sm
            pm += nums[j]; postfixSum[j] = pm
            j -= 1

        for i in range(lth):
            if prefixSum[i] == postfixSum[i]: return i

        return -1

        
