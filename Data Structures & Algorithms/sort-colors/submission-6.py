class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        z = nums.count(0); o = nums.count(1); t = nums.count(2)

        nums.clear()

        if z > 0:
            for i in range(z):
                nums.append(0)


        if o > 0:
            for j in range(o):
                nums.append(1)
        
        if t > 0:
            for k in range(t):
                nums.append(2)
                


            
        