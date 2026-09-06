import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distFromOrigin(x, y):
            return math.sqrt((x) ** 2 + (y) ** 2)

        heap = []

        for point in points:
            x, y = point[0], point[1]

            dist = distFromOrigin(x, y)
            obj = [-dist, point]
            print(point, dist)

            heapq.heappush(heap, obj)

            if len(heap) > k:
                heapq.heappop(heap)

        return [val[1] for val in heap]