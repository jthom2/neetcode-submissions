class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""

        for i in range(min(len(word1), len(word2))):
            s += word1[i] + word2[i]

        if min(len(word1), len(word2)) == len(word1): 
            s += word2[i+1:len(word2)]
        else:
            s += word1[i+1:len(word1)]
        
        return s



        