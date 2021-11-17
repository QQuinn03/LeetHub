class Solution:
    def decodeString(self, s: str) -> str:
        cur_str=""
        cur_val = 0
        stack=[]
 
        for i in s:
            if i.isdigit():
                cur_val=cur_val*10+int(i)
            if i.isalpha():
                cur_str+=i
            if i =="[":
                stack.append(cur_val)
                stack.append(cur_str)
                cur_val=0
                cur_str=""
            if i=="]":
                pre_str=stack.pop()
                pre_val=stack.pop()
                cur_str=pre_str+pre_val*cur_str
        return cur_str        
                
                
                
            