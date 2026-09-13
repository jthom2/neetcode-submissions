class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # res = []

        # for n, c in Counter(nums).items():
        #     if ((c) > (len(nums) // 3)): res.append(n)
        
        

        t = len(nums) // 3; tracked = set(); res = []

        for i, n in enumerate(nums):
            if n in tracked: continue
            tracked.add(n)
            if nums.count(n) > t: res.append(n)

            if len(res) > 1: return res
        
        return res
