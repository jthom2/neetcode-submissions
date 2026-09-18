class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        conseqs = []; count = 0

        for i, n in enumerate(nums):
            if n != 0: count += 1
            else:
                conseqs.append(count)
                count = 0
            if (i == len(nums)-1): conseqs.append(count)

        print(conseqs)
        return max(conseqs)
        