class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        pre = -float("inf")
        res = 0
        
        for start,end in intervals:
            if start>=pre:
                pre=end
            else:
                res+=1
        return res         

