class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        i = 0
        j = 0
        
        heap = []

        while (j < len(nums)):
            heapq.heappush(heap, (-nums[j], j))
            if j - i + 1 > k:
                i += 1
            while heap[0][1] < i:
                heapq.heappop(heap)
            if j - i + 1 == k:
                result.append(-heap[0][0]) 
            j += 1
        return result
