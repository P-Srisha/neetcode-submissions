class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        pairs = {')' : '(', ']' : '[', '}' : '{'}
        # top = -1

        for c in s:
            if c in pairs:
                if not stk:
                    return False
                if stk[-1] != pairs[c]:
                    return False
                stk.pop()
                # top -= 1
            else:
                stk.append(c)
                # top += 1
        return stk == []