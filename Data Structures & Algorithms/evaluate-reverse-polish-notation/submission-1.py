class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        stack = []
        ops = ('+', '-', '*', '/')

        for c in tokens:
            if c in ops:
                b = stack.pop()
                a = stack.pop()
                res = int(eval(f"{a} {c} {b}"))
                stack.append(res)
            else:
                stack.append(int(c))
        return stack[-1] if stack else 0