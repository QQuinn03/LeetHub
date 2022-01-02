class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        
        for i in s:
            while stack and stack[-1]==i:
                stack.pop()
                break
            else:    
                stack.append(i)
        return "".join(stack)    
      