from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        que=deque([])
        time=0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    que.append((i,j,time))
                    grid[i][j]=0
        
        while que:
            i,j,time=que.popleft()
            for i,j in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=i<row and 0<=j<col and grid[i][j]==1:
                    grid[i][j]=2
                    que.append((i,j,time+1))
       
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    return -1
        return time        