class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        maxPro = -1

        while i < j:
            width = j - i
            pro = width * (min(heights[j], heights[i]))

            if pro > maxPro:
                maxPro = pro

            if (heights[i] <= heights[j]):
                i += 1
            elif (heights[j] < heights[i]):
                j -= 1
            
            
            
        return maxPro