class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1,-1]
        res[0]=self.helperL(nums,target)
        res[-1]=self.helperR(nums,target)
        return res
    def helperL(self,nums,target):
        if target not in nums:
            return -1
        l = 0 
        r = len(nums)-1
        
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid]<target:
                l = mid +1
            else:
                r = mid -1
        return l
    
    def helperR(self,nums,target):
        if target not in nums:
            return -1
        l = 0 
        r = len(nums)-1
        
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid]<=target:
                l = mid +1
            else:
                r = mid -1
        if l ==0:
            return 0
        return l-1
        
        
        
        