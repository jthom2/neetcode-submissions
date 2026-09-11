class Solution:

    def encode(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return "null"

        s = "}{".join(strs)

        print(s)

        return s

    def decode(self, s: str) -> List[str]:

        if s == "null":
            return []

        l = s.split('}{')


        return l
