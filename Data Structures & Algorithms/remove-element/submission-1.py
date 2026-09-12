class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        lth = len(nums)
        count = nums.count(val)

        for i in range(count):
            nums.remove(val)

        return (lth - count)


