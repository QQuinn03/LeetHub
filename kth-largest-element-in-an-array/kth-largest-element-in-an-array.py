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
            heapq.heappush(res,i)
        print(heapq.nlargest(k,res))    
        return heapq.nlargest(k,res)[-1] 
            
        # nums.sort()
        # print(nums)
        # return nums[-k]