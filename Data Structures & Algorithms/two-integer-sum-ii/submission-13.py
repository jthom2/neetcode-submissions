class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l < r:
            calc = numbers[l] + numbers[r]

            if calc == target: return [l+1, r+1]
            elif calc < target: l += 1
            elif target < calc: r -= 1                

        return []