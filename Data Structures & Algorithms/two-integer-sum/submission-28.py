class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}; res = []

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diffs:
                return [diffs[diff], i]
            else:  
                diffs[nums[i]] = i
        

        
        return res