class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        start =[]
        end = []
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        
        low = 0
        idx=0
        high=0
        res=[]
        
        while low<len(start):
            merge=[start[low]]
            while low<len(start)-1 and start[low+1]<=end[low]:
                low+=1
            high=low
            merge.append(end[high])
            res.append(merge)
            low+=1
        return res    
                
            