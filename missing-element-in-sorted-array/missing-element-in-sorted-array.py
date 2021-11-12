class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        ans=nums[0]+k
        if len(nums)==1:
            return ans
        for i in (nums[1:]):
            if i>ans:
                return ans
            else:
                ans+=1
        return ans        
        