class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        self.helper(nums,res,path)
        return res
    
    def helper(self,nums,res,path):
        res.append(path)
        for i in range(len(nums)):
            self.helper(nums[i+1:],res,path+[nums[i]])