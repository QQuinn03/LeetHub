class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res=[-1 for i in range(len(nums))]
        stack=[]
        for j in range(2):
            for i in range(len(nums)-1,-1,-1):
                while stack and nums[i]>=nums[stack[-1]]:
                    stack.pop()
                if stack:
                    res[i]=nums[stack[-1]]
                stack.append(i)
        return res        