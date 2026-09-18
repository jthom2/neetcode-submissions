class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        u, d = False, False
        for i in range(1, len(nums)):
            if nums[i-1] <= nums[i]: 
                if d and nums[i] == nums[i-1]:
                    continue 
                u = True
                if d: return False
                continue
            else:
                if nums[i] <= nums[i-1]:
                    if u and nums[i] == nums[i-1]: 
                        continue
                    d = True
                    if u: return False
                    continue
                else: return False

        return True


        