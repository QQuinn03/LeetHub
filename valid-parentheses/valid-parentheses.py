class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in s:
            if i in [")","}","]"]:
                if stack:
                    if i ==")" and stack[-1]!="(":
                        return False
                    elif i =="}"and stack[-1]!="{":
                        return False
                    elif i =="]" and stack[-1]!="[":
                        return False
                    else:
                        stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        return True        
                         
        