class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []

        for n, c in Counter(nums).items():
            if ((c) > (len(nums) // 3)): res.append(n)
        
        return res
