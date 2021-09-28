class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        start=[]
        end = []
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        low = 0
        high=0
        res=0
        start.sort()
        end.sort()
        while low<len(start):
            while low+1<=len(start) and start[low]<end[high]:
                low+=1
                res+=1
            else:
                high+=1
            low+=1
        return res    