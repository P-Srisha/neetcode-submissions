class Solution:
    def isValid(self, s: str) -> bool:
        stk = deque()
        pairs = {')' : '(', ']' : '[', '}' : '{'}

        for c in s:
            if c in pairs:
                if not stk:
                    return False
                if stk[-1] != pairs[c]:
                    return False
                stk.pop()
            else:
                stk.append(c)
        return not stk