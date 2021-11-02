from collections import deque
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        while matrix and matrix[0]:
            
            if matrix and matrix[0]:
                
                res+=matrix.pop(0)
                
            if matrix and matrix[0]:
                for row in matrix:
                    
                    res.append(row.pop())
                    print(res)
            
            if matrix and matrix[-1]:
                res+=matrix.pop()[::-1]
             
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    print(matrix[::-1])
                    res+=[row.pop(0)]
        
        return res
        