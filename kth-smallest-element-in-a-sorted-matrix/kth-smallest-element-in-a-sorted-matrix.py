import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l=matrix[0][0]
        r=matrix[-1][-1]
        res=0
        
        while l<=r:
            mid=l+(r-l)//2
            count,num=self.helper(mid,matrix)
            if count>=k:
                res=num
                r=mid-1
            else:
                l=mid+1
        return res        
                
        
        
    def helper(self, mid, matrix):
        count=0
        num=float("-inf")
        for row in matrix:
            idx=bisect.bisect(row,mid)
            count+=idx
            if idx>0:
                
                num=max(num,row[idx-1])
        return count,num        
        