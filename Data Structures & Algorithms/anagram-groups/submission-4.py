class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []; d = {}; strs.sort()

        lst= strs.copy(); lst=list(map(sorted,lst)); lst= list(map("".join, lst))

    
        for s in lst: d[s] = []

        for i, s in enumerate(lst):
            if s in d: d[s].append(strs[i])

            

        for k, v in d.items():
            if len(v) is None: continue

            res.append(v)
            
        
        return res
        