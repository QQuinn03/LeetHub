class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in ["(","{","["]:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                if i==")":
                    if stack[-1]!="(":
                        return False
                    stack.pop()
                elif i=="}":
                    if stack[-1]!="{":
                        return False
                    stack.pop()
                elif i=="]":
                    if stack[-1]!="[":
                        return False
                    stack.pop()
        if len(stack)!=0:
            return False
        return True
                    
                    