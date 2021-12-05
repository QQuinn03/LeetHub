class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        operand=0
        res=0
        sign=1
        
        for i in s:
            if i.isdigit():
                operand=operand*10+int(i)
                continue
            if i =="+":
                res=res+operand*sign
                sign=1
                operand=0
            elif i =="-":
                res=res+operand*sign
                sign=-1
                operand=0
            elif i=="(":
                stack.append(res)
                stack.append(sign)
                res=0
                sign=1
            elif i==")":
                res+=operand*sign
                res*=stack.pop()
                res+=stack.pop()
                operand=0
                sign=1
        return res+operand*sign        
                
                
                
        