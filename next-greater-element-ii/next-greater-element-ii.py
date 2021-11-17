class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res=[-1]*len(nums)
        stack=[]
        
        for j in range(2):
            for i in range(len(nums)-1,-1,-1):
                while stack and nums[stack[-1]]<=nums[i]:
                    stack.pop()
                if stack:
                    res[i]=nums[stack[-1]]
                stack.append(i)    
        return res            
                