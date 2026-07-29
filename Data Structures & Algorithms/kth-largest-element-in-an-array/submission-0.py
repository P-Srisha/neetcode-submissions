class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        length = len(nums)
        return nums[length-k]