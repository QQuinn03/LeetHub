class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        stack=[]
        for i in logs:
            arr=i.split()
            if arr[1].isdigit():
              
                continue
            stack.append(arr)
        
        stack.sort(key=lambda x:(x[1:],x[0]))
        for i in range(len(stack)):
            a=" ".join(stack[i])
            stack[i]=a            
         
        for i in logs:
            arr=i.split()
            if arr[1].isdigit():
                stack.append(i)
        return stack        
                