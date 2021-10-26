class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
    
        res=1
        idx=0
        pre=points[idx][1]
        while idx<len(points):
            
            if points[idx][0]<=pre:
                idx+=1
            else:
                res+=1
                pre=points[idx][1]
        return res       
            