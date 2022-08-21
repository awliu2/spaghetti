import heapq


class MedianFinder:

    def __init__(self):
        self.lo = [] # maxHeap to store smaller numbers
        self.hi = [] # minHeap to store larger numbers

    def addNum(self, num: int) -> None:
        if not self.lo or not self.hi:
            if not self.hi:
                self.hi.append(num)
            else:
                if self.hi[0] >= num:
                    self.lo.append(-num)
                else:
                    self.lo.append(-self.hi[0])
                    self.hi[0] = num
            
        else:    
            loMax = -self.lo[0]
            hiMin = self.hi[0]

            if len(self.lo) == len(self.hi):
                # currently even num of elements
                if num >= loMax:
                    # simply push num to hi heap
                    heapq.heappush(self.hi, num)
                else:
                    # move an element from lo heap to hi heap

                    heapq.heappush(self.hi, -1 * (heapq.heappop(self.lo)))
                    # add new number to lo heap
                    heapq.heappush(self.lo, -num)
                # should result in len(lo) = len(hi) - 1
            else:
                # currently an odd num of elements and
                # len(lo) = len(hi) - 1
                if num <= hiMin:
                    # simply push new number to lo heap
                    heapq.heappush(self.lo, -num)
                else:
                    # move an element from hi to lo
                    heapq.heappush(self.lo, -1 * (heapq.heappop(self.hi)))
                    # add new num to hi heap
                    heapq.heappush(self.hi, num)
                # should result in len(lo) = len(hi)
        print(f"low: {self.lo}")
        print(f"high: {self.hi}")

    def findMedian(self) -> float:
        if len(self.lo) == len(self.hi):
            return (self.hi[0] - self.lo[0]) / 2 
        else: 
            return self.hi[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()