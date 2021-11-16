class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        right=0
        ks=0
        res=0
        
        while right<len(nums):
            if nums[right]==1:
                pass
            if nums[right]==0:
                ks+=1
            
            
            while ks>k:
                if nums[left]==0:
                    ks-=1

                left+=1
            res=max(res,right-left+1)
            right+=1
        return res    