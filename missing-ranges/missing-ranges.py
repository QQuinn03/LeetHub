class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        pre=lower-1
        cur=0
        res=[]
        
        for i in range(len(nums)+1):
            if i <len(nums):
                cur=nums[i]
            if i >=len(nums):
                cur= upper +1
            if cur >pre+1:
                if cur-1>pre+1:
                    res.append(str(pre+1)+"->"+str(cur-1))
                else:
                   
                    res.append(str(pre+1))
            pre=cur
        return res    