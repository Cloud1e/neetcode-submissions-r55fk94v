class MedianFinder:

    def __init__(self):
        # store larger part
        self.min_heap = []
        # store smaller part
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        # make sure largest num in smaller part is smaller than smallest number in larger part
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        # allow smaller part size is eqaul or 1 larger than larger part
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))


    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()