class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res=0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    res+=1
                    self.dfs(i,j,row,col,grid)
        return res
    
    def dfs(self,i,j,row,col,grid):
        if i<0 or i>=row or j<0 or j>=col or grid[i][j]=="0":
            return 
        grid[i][j]="0"
        
        self.dfs(i+1,j,row,col,grid)
        self.dfs(i-1,j,row,col,grid)
        self.dfs(i,j-1,row,col,grid)
        self.dfs(i,j+1,row,col,grid)
        
        