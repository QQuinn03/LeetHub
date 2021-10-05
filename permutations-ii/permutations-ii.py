class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        check={}
        self.helper(nums,res,[],check)
        return res
        
    def helper (self,nums,res,path,check):
        if not nums:
            if path not in res:
                res.append(path)
                return 
        for i in range(len(nums)):
            current = nums[i]
            rest_nums = nums[:i]+nums[i+1:]
            self.helper(rest_nums,res,path+[current],check)
        return res     