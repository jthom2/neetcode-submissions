class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text); mp = {}

        for c in "balloon": mp[c] = counts[c]

        mp['l'] = mp['l']//2; mp['o'] = mp['o']//2; 

        return min(mp.values())
        