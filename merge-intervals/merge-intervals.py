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
        
        #  1 2  8  15
        #  3 6  10 18
        
        while idx <len(end):
            val1=start[idx]
            while idx+1<len(start) and start[idx+1]<=end[idx]:
                idx+=1
            else:
                val2=end[idx]
            idx+=1    
            arr=[val1,val2]
            res.append(arr)
        return res    
            
        
   
                