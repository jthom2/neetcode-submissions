class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []

        # for n, c in Counter(nums).items():
        #     if ((c) > (len(nums) // 3)): res.append(n)
        

        l = len(nums); s = set()

        for i, n in enumerate(nums):
            if (n not in s):
                if (nums.count(n) > l//3):
                    s.add(n)
                    res.append(n)
                


        
        
        return res
