class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = []
        for i in range(1,10):
            nums.append(i)
        res=[]
        self.helper(nums,[],res,k,n)
        return res
    
    def helper(self,nums,path,res,k,n):
        if len(path)>=k:
            if sum(path)==n and len(path)==k:
                res.append(path)
                return 
            else:
                return 
        for i in range(len(nums)):
            self.helper(nums[i+1:],path+[nums[i]],res,k,n)