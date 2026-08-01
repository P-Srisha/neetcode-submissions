class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        leftMax, rightMax = [0] * length, [0] * length
        minMax = []
        for i in range(1, length):
            leftMax[i] = max(leftMax[i - 1], height[i - 1])
        for i in range(length - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i + 1])
        for i in range(length):
            minMax.append(min(leftMax[i], rightMax[i]))

        water = 0
        for i in range(length):
            if minMax[i] - height[i] >= 0:
                water += minMax[i] - height[i]
        print(minMax)
        return water