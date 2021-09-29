import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        
        for i in points:
            heapq.heappush(arr,((i[0]**2+i[1]**2),i))
        
        res=[]
        for i in range(k):
            distance=heapq.heappop(arr)
            res.append(distance[1])
        return res    
            
        