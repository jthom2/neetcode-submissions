class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}; l = 0; ml = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]]+1, l)
            mp[s[r]] = r
            ml = max(ml, r-l+1)
        return ml

    
        