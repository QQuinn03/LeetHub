class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        idx=0
        while i<len(nums):
            if nums[i]==val:
                i+=1
            else:
                nums[idx],nums[i]=nums[i],nums[idx]
                idx+=1
                i+=1
        return idx          