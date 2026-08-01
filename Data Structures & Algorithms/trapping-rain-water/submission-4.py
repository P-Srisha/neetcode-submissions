class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        l, r = 0, len(height) - 1
        water = 0
        maxL, maxR = height[l], height[r]

        while (l < r):
            if (maxL <= maxR):
                l += 1
                if height[l] > maxL:
                    maxL = height[l]
                water += maxL - height[l]
            else:
                r -= 1
                if height[r] > maxR:
                    maxR = height[r]
                water += maxR - height[r]
        return water