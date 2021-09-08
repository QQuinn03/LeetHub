class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end =[]
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        
        res = 0
        idx = 0
        high = 0
        while idx<len(start):
            
            while idx<=len(start)-1 and start[idx]<end[high]:
                res+=1
                idx+=1
            else:
                high+=1
            idx+=1
        return res    
                
            