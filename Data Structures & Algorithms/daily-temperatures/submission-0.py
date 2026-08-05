class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:     
        stk = list()
        length = len(temperatures)
        result = [0] * length

        for i in range(length):
            curr = temperatures[i]
            while stk and curr > stk[-1][0]:
                popped = stk.pop()
                result[popped[1]] = i - popped[1]
            stk.append([curr, i])

        return result           