class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        res=0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j]!=0:
                    seen=set()
                    temp=self.helper(grid,row,col,i,j,seen)
                    res=max(res,temp)
        return res
    
    def helper(self,grid,row,col,i,j,seen):
        if i<0 or i>=row or j<0 or j>=col or (i,j) in seen or grid[i][j]==0:
            return 0
        seen.add((i,j))
        cur_val=grid[i][j]
        l=self.helper(grid,row,col,i,j-1,seen)
        r=self.helper(grid,row,col,i,j+1,seen)
        u=self.helper(grid,row,col,i+1,j,seen)
        d=self.helper(grid,row,col,i-1,j,seen)
        seen.remove((i,j))
        return cur_val+max(l,max(r,max(u,d)))
        
        