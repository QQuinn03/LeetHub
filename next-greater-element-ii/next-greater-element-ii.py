class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        res=[-1]*len(nums)
        size=len(nums)
        for i in range(size*2-1,-1,-1):
            while stack and stack[-1]<=nums[i%size]:
                
                stack.pop()
            if stack:
                res[i%size]=stack[-1]
            stack.append(nums[i%size]) 
        return res    
                