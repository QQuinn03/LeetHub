class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        res = float("inf")
        total=0
        while right<len(nums):
            total +=nums[right]
            while total>=target:
                res = min(res,right-left+1)
                total-=nums[left]
                left+=1
            right+=1
        
        return res if res<float("inf") else 0
