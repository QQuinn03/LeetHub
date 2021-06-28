class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums)-1
        
        while l<=r:
            mid = l +(r-l)//2
            if nums[mid]==target:
                return True
            while l < mid and nums[l] == nums[mid]: # tricky part
                l += 1
            if nums[mid]>=nums[l]:
                if target>=nums[l]and target<nums[mid]:
                    r = mid -1
                else:
                    l = mid+1
            else:
                if target>nums[mid] and target<=nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return False           
        
        