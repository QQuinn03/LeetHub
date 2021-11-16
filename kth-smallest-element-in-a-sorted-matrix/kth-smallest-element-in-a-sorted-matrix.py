import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq=[]
        for i in matrix:
            idx=0
            heapq.heappush(pq,(i[idx],i,idx))
         
        res=[]
        while pq:
            val,arr,idx=heapq.heappop(pq)
            res.append(val)
            if idx+1<len(arr):
                heapq.heappush(pq,(arr[idx+1],arr,idx+1))

        return res[k-1]         
            
            