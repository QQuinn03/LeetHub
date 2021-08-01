class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height)-1
        
        while left<right:
            left_contain = height[left]
            right_contain = height[right]
            if left_contain<right_contain:
                res = max(res,(right-left)*left_contain)
                left+=1
            else:
                res = max(res,(right-left)*right_contain)
                right-=1
        return res         
                
                