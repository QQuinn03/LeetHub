class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack=[]
        seen=set()
        dic={}
        
        for i in range(len(s)):
            dic[s[i]]=i
            
        for idx,char in enumerate(s):
            if char not in seen:
                while stack and stack[-1]>char and idx<dic[stack[-1]]:
                    seen.remove(stack[-1])
                    stack.pop()
                stack.append(char)
                seen.add(char)
        return "".join(stack)         