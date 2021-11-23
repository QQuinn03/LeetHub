import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        que=[]
        for point in points:
            if len(que)==k:
                heapq.heappushpop(que,(-(point[0]**2+point[1]**2),point))
            else:
                heapq.heappush(que,(-(point[0]**2+point[1]**2),point))
        res=[]
        for i in que:
            res.append(i[1])
        return res    
            
       