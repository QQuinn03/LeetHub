class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=0
        left=0
        right=1
        #11345  0
        
        while left<len(nums) and right<len(nums):
            if left==right or nums[right]-nums[left]<k:
                right+=1
            elif nums[right]-nums[left]>k:
                left+=1
            else:
                res+=1
                left+=1
                while left<len(nums)and nums[left]==nums[left-1]:
                    left+=1
        return res            
                