class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic={0:1}
        res=0
        total=0
        
        for i in nums:
            total+=i
            if total-k in dic:
                res+=dic[total-k]
            if total not in dic:
                dic[total]=1
            else:
                dic[total]+=1
        return res        

    
             
     