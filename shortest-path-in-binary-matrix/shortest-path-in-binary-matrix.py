from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        que = deque([(0,0,1)])
        grid[0][0]=1
        
        while que:
            
            i,j,d = que.popleft()
            
            if i==n-1 and j==n-1:
                return d
            for a, b in ((i-1, j-1), (i+1, j+1), (i-1, j), (i+1, j), (i, j-1), (i, j+1), (i-1, j+1), (i+1, j-1)):
                if 0 <= a < n and 0 <= b < n and grid[a][b] == 0:
                    grid[a][b] = 1
                    que.append((a, b, d+1))
        return -1          
        