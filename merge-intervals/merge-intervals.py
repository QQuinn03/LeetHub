class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        start =[]
        end = []
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        
        intveral=[]
        idx=0
        low=0
        high=0
        res=[]
        while idx<len(start):
            low=idx
            while idx<len(start)-1 and start[idx+1]<=end[idx]:
                idx+=1
               
            high=idx
            res.append([start[low],end[high]])
            idx+=1
        return res     
        
 