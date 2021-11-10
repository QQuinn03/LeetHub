class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic={0:1}
        
        res=0
        total=0
        for i in nums:
            total+=i
            if total-k in dic:
                res+=dic[total-k]
            if total in dic:
                dic[total]+=1
            if total not in dic:
                dic[total]=1
        return res        
            
            