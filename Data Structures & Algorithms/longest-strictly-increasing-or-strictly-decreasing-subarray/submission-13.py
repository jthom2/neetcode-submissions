class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        count = 0; counts = []; stack_i = []; stack_d = [];

        if len(nums) == 1: return 1

        ic = 0; dc = 0; i = False; d = False

        for i, n in enumerate(nums):
            if not stack_i: stack_i.append(n)
            else:
                if stack_i[-1] < n: stack_i.append(n)
                elif stack_i[-1] > n:
                    counts.append(len(stack_i))
                    stack_i.clear()
                    stack_i.append(n)
            if not stack_d: stack_d.append(n)
            else:
                if n < stack_d[-1]: stack_d.append(n)
                elif n > stack_d[-1]:
                    counts.append(len(stack_d))
                    stack_d.clear()
                    stack_d.append(n)
                else:
                    counts.append(len(stack_d))
                    counts.append(len(stack_i))
                    stack_d.clear()
                    stack_d.append(n)
                    stack_i.clear()
                    stack_i.append(n)
            if (i == len(nums)-1):
                counts.append(len(stack_d))
                counts.append(len(stack_i))
        #     print(i,"   ", stack_d)
            
        # print(counts)



        if counts: return max(counts)
        else: return -1
