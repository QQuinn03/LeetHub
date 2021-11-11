class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
 
        idx=0
        cur_num=0
        cur_str=""
        while idx<len(s):
            if s[idx].isdigit():
                cur_num=cur_num*10+int(s[idx])
            elif s[idx].isalpha():
                cur_str+=s[idx]    
            elif s[idx]=="[":
                stack.append(cur_str)
                stack.append(cur_num)
                
                cur_num=0
                cur_str=""
            else:
                
                val_num=stack.pop()
                pre_str=stack.pop()
                
                cur_str=pre_str+cur_str*val_num
               
            idx+=1    
        return cur_str
                
                
            