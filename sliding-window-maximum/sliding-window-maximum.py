from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack=deque([])
        res=[]
        
        for idx,val in enumerate(nums):
            while stack and nums[stack[-1]]<val:
                stack.pop()
            stack.append(idx)
            
            if stack[0]==idx-k:
                stack.popleft()
            if stack[-1]>=k-1:
                res.append(nums[stack[0]])
        print(res)   
        return res
                