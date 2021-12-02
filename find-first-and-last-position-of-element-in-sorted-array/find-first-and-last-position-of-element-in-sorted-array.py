class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        res=[-1,-1]
        res[0]=self.left(nums,target)
        res[1]=self.right(nums,target)
        
        return res
    
    def left(self,nums,target):
        if target not in nums:
            return -1
        l=0
        r=len(nums)-1
        
        while l<r:
            mid=l+(r-l)//2
            if nums[mid]>=target:
                r = mid
            elif nums[mid]<target:
                l = mid+1
        return l 
    
    def right(self,nums,target):
        if target not in nums:
            return -1
        l=0
        r=len(nums)-1
        
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]>target:
                r = mid-1
            if nums[mid]<=target:
                l=mid+1
                
        return l-1  
        