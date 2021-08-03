class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.helper(candidates,res,[],target)
        return res
    
    def helper(self,candidates,res,path,target):
        if sum(path)>target:
            return
        if sum(path)==target:
            res.append(path)
            return
        for i in range(len(candidates)):
            self.helper(candidates[i:],res,path+[candidates[i]],target)