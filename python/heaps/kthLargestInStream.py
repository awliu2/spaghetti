import heapq
from typing import List

# Design a class to find the kth largest element in a stream. 
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minHeap with size k
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    # int add(int val) Appends the integer val to the stream, 
    # returns the element representing the kth largest element in the stream.
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)