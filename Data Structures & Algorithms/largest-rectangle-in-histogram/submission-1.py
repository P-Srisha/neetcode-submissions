class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        maxA = 0

        for i in range(len(heights)):
            start = i
            while stk and stk[-1][1] > heights[i]:
                index, height = stk.pop()
                maxA = max(maxA, (i - index) * height)
                start = index
            stk.append([start, heights[i]])
            
        for i, h in stk:
            maxA = max(maxA, h * (len(heights) - i))
        return maxA