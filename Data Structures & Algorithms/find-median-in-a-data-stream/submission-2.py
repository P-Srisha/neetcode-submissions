import heapq

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if self.minHeap and num < self.minHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        elif self.maxHeap and num > -self.maxHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.minHeap, num)

        imb = len(self.minHeap) - len(self.maxHeap)

        if imb == 2:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)
        if imb == -2 or imb == -1:
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)

    def findMedian(self) -> float:
        n = len(self.minHeap) + len(self.maxHeap)

        if n % 2 == 0:
            return (self.minHeap[0] + -self.maxHeap[0]) / 2
        
        return self.minHeap[0]