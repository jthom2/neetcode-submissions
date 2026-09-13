class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []; l = len(nums);

        # try:
        #     for i in range(l):
        #         if (nums.count(nums[i]) > n) and (nums[i] not in res): res.append(nums[i])
        # except:
        #     print("FUCKED") 
        #     return [8, 0, 0, 8]

        count = Counter(nums); print(count)

        for n, c in count.items():
            if c > l // 3: res.append(n)
        


        return res