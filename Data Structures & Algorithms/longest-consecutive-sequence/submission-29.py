class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0: return 0        

        mac, macs = 1, []


        nums = (list(set(nums)))
        nums.sort()
        dnums = {value: index for index, value in enumerate(nums)}         
        l = len(nums)


        for i, n in enumerate(nums):
            if (n-1 not in dnums) and (i != l-1) and (n == nums[i+1] - 1):
                mac += 1
            elif (i != l-1) and (n == nums[i + 1] - 1):
                mac += 1
            elif (i != l-1) and (n != nums[i+1] - 1):
                macs.append(mac)
                mac = 1
            elif (i == l-1):
                macs.append(mac)
                mac = 1

        if macs: return max(macs)       
        return 0
                