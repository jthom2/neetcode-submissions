class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        words.sort(key=len)

        for w in words:
            for wrd in words:
                if w == wrd: continue
                elif w in wrd:
                    res.append(w)
                    break
                
        return res

        
        