import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res =[]
      
        for i in nums:
            if len(res)<k:
                heapq.heappush(res,i)
            else:
                heapq.heappushpop(res,i)
        return res[0]        