import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while heap:
            x = -heapq.heappop(heap)

            if not heap:
                return x

            y = -heapq.heappop(heap)

            if x == y:
                continue
            
            if x != y:
                heapq.heappush(heap, y - x)

        return 0