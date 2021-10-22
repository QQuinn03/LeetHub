class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        res=1
        pre=points[0][1]
        
        for i in points:
            if i[0]>pre:
                res+=1
                pre=i[1]
            
        return res        