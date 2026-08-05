class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        comb = [[p, s] for p, s in zip(position, speed)]
        comb.sort()
        stk = list()
        length = len(position)
        count = 0

        for i in range(length - 1, -1, -1):
            curr = (target - comb[i][0]) / comb[i][1]
            stk.append(curr)
            if len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop()
            
        return len(stk)