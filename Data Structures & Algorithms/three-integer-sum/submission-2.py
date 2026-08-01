class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        j = len(nums) - 1
        k = 0

        nums.sort()

        numSet = set(nums)

        result = set()
        for k in range(len(nums)):
            i = k + 1
            j = len(nums) - 1
            ele = nums[k]
            target = -ele

            while (i <= j):
                s = nums[i] + nums[j]
                if s == target and i != j:
                    result.add((ele, nums[i], nums[j]))
                    i += 1
                    j -= 1
                elif s < target:
                    i += 1
                else:
                    j -= 1


        return [list(x) for x in result]