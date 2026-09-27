class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        m = {}

        for i in range(len(nums)):
            target = -nums[i]

            l = 0; r = len(nums)-1
            while l<r:
                if nums[l] + nums[r] > target:
                    r -= 1
                    continue
                elif nums[l] + nums[r] < target:
                    l += 1
                    continue
                else:
                    if i != l and i != r and l != r:
                        n = [nums[i], nums[l], nums[r]]
                        n.sort()
                        n = tuple(n)
                        if n not in m:
                            m[n] = i
                l += 1
                r -= 1

  

        return list(map(list, m.keys()))

        