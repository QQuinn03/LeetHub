class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res=0
        start=[]
        end=[]
        
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        
        low=0
        high=0
        
        while low<len(start):
            while low<=len(start)-1 and start[low]<end[high]:
                res+=1
                low+=1
            else:
                high+=1
            low+=1
        return res     
        
