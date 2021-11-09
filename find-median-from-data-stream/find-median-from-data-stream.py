from collections import deque
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap=[]
        self.min_heap=[]

    def addNum(self, num: int) -> None:
        if len(self.max_heap)==0:
            heapq.heappush(self.max_heap,-num)
            return 
        
        if num<=-self.max_heap[0]:
            heapq.heappush(self.max_heap,-num)
        else:
            heapq.heappush(self.min_heap,num)
        
        if len(self.max_heap)-len(self.min_heap)==2:
            val = -heapq.heappop(self.max_heap)
            print(val)
            heapq.heappush(self.min_heap,val)
        elif len(self.min_heap)-len(self.max_heap)==2:
            val=heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-val)
            

    def findMedian(self) -> float:
        
        if len(self.max_heap)==len(self.min_heap):
            val1=-self.max_heap[0]
            val2=self.min_heap[0]
        
            return float((val1+val2)/2)
        elif len(self.max_heap)>len(self.min_heap):
            return -self.max_heap[0]
        return float(self.min_heap[0]) 


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()