class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    res+=1
                    self.helper(grid,i,j,row,col)
        return res
    
    
    def helper(self,grid,i,j,row,col):
        if i<0 or j <0 or i>=row or j >=col or grid[i][j]=="0":
            return 
        grid[i][j]="0"
        self.helper(grid,i+1,j,row,col)
        self.helper(grid,i-1,j,row,col)
        self.helper(grid,i,j+1,row,col)
        self.helper(grid,i,j-1,row,col)
        