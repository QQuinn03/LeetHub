from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        sign=1
        res=0
        operand = 0
        
        for i in s:
            if i.isdigit():
                operand=operand*10+int(i)
            elif i =="-":
                res+=operand*sign
                sign=-1
                operand=0
            elif i=="+":
                res+=operand*sign
                sign=1
                operand =0
            elif i=="(":
                stack.append(res)
                stack.append(sign)
                res=0
                sign=1
                operand=0
            elif i==")":
                res+=operand*sign
                res*=stack.pop()
                res+=stack.pop()
                operand=0

        return res+operand*sign        
        
                    
  
            
        
     