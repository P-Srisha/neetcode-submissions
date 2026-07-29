import random

class Solution:            
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(left, right):
            if left == right: return nums[left]
            
            # Randomly pick a pivot to avoid O(n^2) worst case and recursion depth issues
            pivot_index = random.randint(left, right)
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            
            pivot = nums[right]
            p = left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[right] = nums[right], nums[p]

            if p > k:
                return quickSelect(left, p-1)
            elif p < k:
                return quickSelect(p+1, right)
            else:
                return nums[p]  

        return quickSelect(0, len(nums) - 1)