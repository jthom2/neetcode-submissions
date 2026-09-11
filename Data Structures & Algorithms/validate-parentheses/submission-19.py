class Solution:
    def isValid(self, s: str) -> bool:
        
        opened = ['(', '{', '[']
        closed = [')', '}', ']']

        opens = {
            '(': 0,
            '{': 1,
            '[': 2
        }

        closes = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []


        for i, c in enumerate(s):
            if c in opened:
                stack.append(c)


            if c in closed:

                if closes[c] not in stack:
                    return False
                
                if stack[-1] != closes[c]:
                    return False

                stack.pop()

        if stack:
            return False






        return True