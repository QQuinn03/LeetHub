class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        start =[]
        end = []
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        
        res=[]
        idx = 0
        high=0
        low=0
        
        while idx<len(start):
            low = idx
            path = []
            while idx<len(start)-1 and start[idx+1]<=end[idx]:
                idx+=1
            high=idx
            
            path.append(start[low])
            path.append(end[high])
            res.append(path)
            
            
            
            idx+=1
        return res     
                