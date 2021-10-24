class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack=[]
        check=None
        for i in preorder:
            while stack and i>=stack[-1]:
                check=stack.pop()
            if check!=None and check>i:
                return False
            stack.append(i)
        return True    
            