import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        # heapify(heap)
        for i in nums:
            if len(heap)<k:
                heapq.heappush(heap,i)   
            else:
                heapq.heappushpop(heap,i)
        print(heap)    
        return heap[0]