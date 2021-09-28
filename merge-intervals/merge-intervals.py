class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        start=[]
        end = []
        
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
            
        start.sort()
        end.sort()
        res=[]
        idx=0
        while idx<len(start):
            arr=[]
            arr.append(start[idx])
            while idx+1<len(start)and start[idx+1]<=end[idx]:
                idx+=1
            high=idx
            arr.append(end[high])
            res.append(arr)
            idx+=1
        return res    
            
                
        