class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for i in num:
            while k and stack and int(stack[-1])>int(i):
                stack.pop()
                k-=1
            stack.append(i)
     
        while k!=0:
            stack.pop()
            k-=1
        i=0
        while i<len(stack) and stack[i]=="0":
            i+=1
        if len(stack[i:])>0:
            return "".join(stack[i:])
        else:
            return "0"
            