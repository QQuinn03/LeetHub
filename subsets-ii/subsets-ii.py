class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        self.helper(sorted(nums),res,path)
        return res
    
    def helper(self,nums,res,path):
        if path not in res:
            res.append(path)
         
        for i in range(len(nums)):
            if i >0 and nums[i]==nums[i-1]:
                continue
            self.helper(nums[i+1:],res,path+[nums[i]])    