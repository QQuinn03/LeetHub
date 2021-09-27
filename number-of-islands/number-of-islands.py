class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or len(grid)==0:
            return 0
        row = len(grid)
        col = len(grid[0])
   
        count=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    count+=1
                    self.helper(grid,i,j,row,col)
        return count
    
    def helper(self,grid,i,j,row,col):
        if i <0 or i>=row or j<0 or j>=col or grid[i][j]=="0":
            return
        grid[i][j]="0"
        
        self.helper(grid,i+1,j,row,col)
        self.helper(grid,i-1,j,row,col)
        self.helper(grid,i,j+1,row,col)
        self.helper(grid,i,j-1,row,col)
                    


        
        