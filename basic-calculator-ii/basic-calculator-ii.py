class Solution:
    def calculate(self, s: str) -> int:
        flag="+"
        res=[]
        temp=0
        for i in range(len(s)):
            if s[i].isdigit():
                temp=temp*10+int(s[i])
            if s[i] in ["+","-","*","/"] or i ==len(s)-1:
                if flag=="+":
                    res.append(temp)
                elif flag=="-":
                    res.append(-temp)
                elif flag=="*":
                    val = res.pop()
                    res.append(val*temp)
                else:
                    val = res.pop()
                    res.append(int(val/temp))
                flag=s[i]    
                temp=0     
                    
                    
                
            
        return sum(res)           
                    
                    
                    
                