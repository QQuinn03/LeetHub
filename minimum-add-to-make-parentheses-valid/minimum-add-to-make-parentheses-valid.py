class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack1=[]
        stack2=[]
        
        for i in range(len(S)):
            if S[i] =="(":
                stack1.append(S[i])
            elif S[i]==")" and stack1:
                stack1.pop()
            else:
                stack2.append(S[i])
        print(stack1,stack2)        
        return len(stack1)+len(stack2)        
        