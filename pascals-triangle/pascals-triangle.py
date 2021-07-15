class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            l=[1]
            res.append((i+1)*l)
        
        for i in range(2,numRows):
            for j in range(i):
                if j == 0 or j ==-1:
                    continue 
                res[i][j]= res[i-1][j]+res[i-1][j-1]
        return res        
            
            