class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack =[]
        node = None
        for val in preorder:
            while stack and val>stack[-1]:
                node = stack.pop()
            if node !=None and node>val:
                return False
            stack.append(val)
        return True    