class Solution:
    def decodeString(self, s: str) -> str:
        cur_val=0
        stack=[]
        cur_string=""
        
        for i in s:
            if i.isdigit():
                cur_val = cur_val*10 +int(i)
            elif i.isalpha():
                cur_string+=i
            elif i=="[":
                stack.append(cur_val)
                stack.append(cur_string)
                cur_val=0
                cur_string=""
            else:
                pre_str=stack.pop()
                pre_val=stack.pop()
                cur_string=pre_str+cur_string*pre_val
          
        return cur_string                
                
            