class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        for num in nums:
            pro *= num
        rs = [pro for _ in range(len(nums))]
        for i in range(len(nums)):
            if nums[i] == 0:
                rs[i] = 1
                for j in range(len(nums)):
                    if (i != j):
                        rs[i] *= nums[j]
            else: 
                rs[i] //= nums[i]
        return rs