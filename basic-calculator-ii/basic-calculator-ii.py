class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        operand = 0
        sign = "+"
        for i in range(len(s)):
            if s[i].isdigit():
                operand = operand*10+int(s[i])
            if s[i] in ['+', '-', '*', '/'] or i ==len(s)-1:
                if sign =="+":
                    stack.append(+operand)
                elif sign =="-":
                    stack.append(-operand)
                elif sign == "*":
                    val = stack.pop()
                    stack.append(val*operand)
                else:
                    val = stack.pop()
                    stack.append(int(val/operand))
                sign = s[i]
                operand = 0
      
        return sum(stack)         
            
            