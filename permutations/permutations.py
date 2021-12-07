class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        path=[]
        res=[]
        self.helper(nums,res,path)
        return res
        
    
    def helper(self,nums,res,path):
        if not nums:
            res.append(path)
            return res
        
        for i in range(len(nums)):
            cur = nums[i]
            left=nums[:i]+nums[i+1:]
            self.helper(left,res,path+[cur])
       