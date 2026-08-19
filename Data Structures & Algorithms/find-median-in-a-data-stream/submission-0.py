import heapq
class MedianFinder:

    def __init__(self):
        self.sm =[]
        self.lr =[]

    def addNum(self, num: int) -> None:
        if not self.sm or -self.sm[0]>=num:
            heapq.heappush(self.sm, -num)
        else:
            heapq.heappush(self.lr, num)
        if len(self.sm)> len(self.lr)+1:
            lr = -heapq.heappop(self.sm)
            heapq.heappush(self.lr, lr)
        elif len(self.sm)<len(self.lr):
            heapq.heappush(self.sm, -heapq.heappop(self.lr))

    def findMedian(self) -> float:
        if len(self.sm) ==len(self.lr):
            return (-self.sm[0]+self.lr[0])/2
        else:
            return -self.sm[0]
        
        