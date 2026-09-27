class Solution:

    def encode(self, strs: List[str]) -> str:
        if  len(strs) ==  0: return  "null"
        encoded_string = "}{".join(strs)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if s == "null": return []
        decoded_string = s.split("}{")
        return decoded_string