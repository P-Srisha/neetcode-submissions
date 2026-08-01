class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue

            if nums[k] > 0:
                break

            i = k + 1
            j = len(nums) - 1

            while (i < j):
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    result.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif s < 0:
                    i += 1
                else:
                    j -= 1

        return result