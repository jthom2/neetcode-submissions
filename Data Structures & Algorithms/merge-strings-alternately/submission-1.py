class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0; r = min(len(word1), len(word2))-1

        s = ""
        j = 0
        for i in range(min(len(word1), len(word2))):
            s += word1[i] + word2[i]

            j = i

        print(s)
        if min(len(word1), len(word2)) == len(word1): 
            s += word2[j+1:len(word2)]
        else:
            s += word1[j+1:len(word1)]
        

        

        return s



        