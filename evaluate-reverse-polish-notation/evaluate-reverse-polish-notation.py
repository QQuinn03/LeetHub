class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for i in tokens:
            if i not in["+","-","*","/"]:
                res.append(int(i))
                continue
            num1 = res.pop()
            num2 = res.pop()
            if i=="-":
                res.append(num2-num1)
            elif i =="+":
                res.append(num2+num1)
            elif i =="*":
                res.append(num2*num1)
            else:
                res.append(int(num2/num1))
        return sum(res)       
                
                
                
                