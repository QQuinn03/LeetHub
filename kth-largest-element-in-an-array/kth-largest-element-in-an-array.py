import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        que=[]
        for i in nums:
            if len(que)==k:
                heapq.heappushpop(que,i)
            else:
                heapq.heappush(que,i)
             
        return que[0]         