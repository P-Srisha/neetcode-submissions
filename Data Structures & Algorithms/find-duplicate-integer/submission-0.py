class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cnt = set()

        for i in nums:
            if i in cnt:
                return i
            cnt.add(i)