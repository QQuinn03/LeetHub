class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        start =[]
        end = []
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        
        low=0
        high=0
        idx=0
        res=[]
        
        while idx<len(start):
            low=idx
            while idx+1<len(start) and start[idx+1]<=end[idx]:
                idx+=1
            high=idx
            arr=[start[low],end[high]]
            res.append(arr)
            idx+=1
        return res     
     