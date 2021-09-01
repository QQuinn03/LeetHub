class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if self.binary_search(row,target)==True:
                return True
        return False    
    
    def binary_search(self,nums,target):
        l = 0
        r = len(nums)-1
        
        
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return True
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1