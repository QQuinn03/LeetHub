class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left={}
        right={}
        count={}
        for i in range(len(nums)):
            right[nums[i]]=i
            if nums[i] not in left:
                left[nums[i]]=i
                
            count[nums[i]]=count.get(nums[i],0)+1
        
        degree=max(count.values())
        ans = len(nums)
        for i in count:
            if count[i]==degree:
                ans=min(ans,right[i]-left[i]+1)
        return ans        
                  
                