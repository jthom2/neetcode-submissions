class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sub = []; sublst = []; sms = []; sm = 0

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                if sm == 0: sm = nums[i-1] + nums[i]
                else: sm += nums[i]
            else:
                sms.append(sm)
                sms.append(nums[i-1])
                sm = nums[i]

        sms.append(sm)
                
            
        
        


        if sms: return max(sms)
        else: return 0