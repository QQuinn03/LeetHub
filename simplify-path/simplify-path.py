class Solution:
    def simplifyPath(self, path: str) -> str:
        path_=path.split("/")
        stack=[]
        
        for i in path_:
            if i=="..":
                if stack:
                    stack.pop()
            elif i =="." or not i:
                continue
            else:
                stack.append(i)
        return "/"+"/".join(stack)        
       
   