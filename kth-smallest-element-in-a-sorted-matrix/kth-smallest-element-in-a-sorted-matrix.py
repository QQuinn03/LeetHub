import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        que=[]

        for i in matrix:
            idx=0
            heapq.heappush(que,(i[idx],i,idx))
        res=[]
        
        while que:
            val,arr,idx=heapq.heappop(que)
            res.append(val)
            if idx+1<=len(arr)-1:
                idx+=1
      
                heapq.heappush(que,(arr[idx],arr,idx))
        return res[k-1]       