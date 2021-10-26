class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len1 = len(num1)-1
        len2 = len(num2)-1
        carry = 0
        res=[]
        temp1 = temp2 = 0
        while len1>=0 or len2>=0:
            if len1>=0:
             
                temp1 = ord(num1[len1])-ord("0")
            if len2>=0:
                temp2 = ord(num2[len2])-ord("0")
                
            temp = temp1+temp2+carry
            
            carry=temp//10
            temp=temp%10
            
            res.append(str(temp))
            temp1 = temp2=0
            len1-=1
            len2-=1
       
        if carry ==1:
            res.append("1")
        return "".join(res[::-1])  
           
             
                
        
        