class Solution:
    def simplifyPath(self, path: str) -> str:
       
        stack =[]
        temp = path.split("/")
        
        for i in temp:
            if i =="..":
                if stack:
                    stack.pop()
            elif i =="." or not i:
                continue
            else:
                stack.append(i)
        print(stack)
        return "/"+"/".join(stack)
                
        
        
                