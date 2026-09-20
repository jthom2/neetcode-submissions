class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for i, t in enumerate(tokens):
            try: s.append(int(t))
            except:
                op1 = s.pop(); op2 = s.pop()
                if t == '+': s.append(op1 + op2)
                elif t == '-': s.append(op2 - op1)
                elif t == '*': s.append(op1 * op2)
                elif t == '/': s.append(int(op2/op1))

        return s[0]    