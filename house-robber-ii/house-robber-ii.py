class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        dp_1 = [[0] for i in range(len(nums)-1)]
        dp_1[0]=nums[0]
        dp_1[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)-1):
            dp_1[i]=max(nums[i]+dp_1[i-2],dp_1[i-1])
        res1=dp_1[-1]   
        
        dp_2 = [[0] for i in range(len(nums)-1)]
        dp_2[0]= nums[1]
        dp_2[1]=max(nums[1],nums[2])
        for i in range(2,len(dp_2)):
            dp_2[i]=max(nums[i+1]+dp_2[i-2],dp_2[i-1])
        
        return max(res1,dp_2[-1])
            
        
        