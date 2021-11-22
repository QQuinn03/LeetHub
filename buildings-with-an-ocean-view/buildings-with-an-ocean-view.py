class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack=[]
        
        for i,val in enumerate(heights):
            while stack and heights[stack[-1]]<=val:
                stack.pop()
            stack.append(i)
        return stack    