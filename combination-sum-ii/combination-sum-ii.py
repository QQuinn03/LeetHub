class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res =[]
        candidates.sort()
        self.helper(candidates,res,path,target)
        return res
    def helper(self,candidates,res,path,target):
        if target<0:
            return 
        if target==0:
            res.append(path)
        for i in range(len(candidates)):
            if i>0 and candidates[i]==candidates[i-1]:
                continue
            self.helper(candidates[i+1:],res,path+[candidates[i]],target-candidates[i])