class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = len(nums); s = set(); res = []; b = {}

        for i, n in enumerate(nums):
            if (n not in b): 
                b[n] = nums.count(n)
            if (n not in s):
                if (b[n] > l//3):
                    s.add(n)
                    res.append(n)
        
        return res
