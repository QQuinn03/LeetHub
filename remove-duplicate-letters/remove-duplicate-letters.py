class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack=[]
        last_seen ={c:i for i,c in enumerate(s)}
        seen = set()
        for i,c in enumerate(s):
            if c not in seen:
                while stack and c<stack[-1] and i<last_seen[stack[-1]]:
                    print(i,stack[-1])
                    pop = stack.pop(-1)
                    seen.remove(pop)
                seen.add(c)
                stack.append(c)
        return "".join(stack)          
                    
            