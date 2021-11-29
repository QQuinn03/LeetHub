class Solution:
    def removeDuplicates(self, s: str) -> str:
        dic={}
        for i in range(len(s)):
            dic[s[i]]=i
        
        stack=[]
        seen=set()
        for idx,char in enumerate(s):
            while stack and stack[-1]==char:
                stack.pop()
                break
            else:    
                stack.append(char)
        return "".join(stack) 
            