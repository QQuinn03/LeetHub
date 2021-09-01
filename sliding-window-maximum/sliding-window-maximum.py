from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque([])
        output =[]
        
        for idx,val in enumerate(nums):
            while que and nums[que[-1]]<val:
                que.pop()
            que.append(idx)
            
            if que[0]==idx-k:
                que.popleft()
            if que[-1]>=k-1:
                output.append(nums[que[0]])
           
            
        return output        
        
        
        