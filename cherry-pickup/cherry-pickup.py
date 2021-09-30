class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        check= {}
        
        res = self.helper(grid,n,0,0,0,0,check)
        if res>0:
            return res
        else:
            return 0
        
    def helper(self,grid,n,x1,y1,x2,y2,check):
        if x1==n-1 and y1==n-1:
            return grid[x1][y1] if grid[x1][y1]!=-1 else float("-inf")
        
        if x1==n or y1==n or x2==n or y2==n or grid[x1][y1]==-1 or grid[x2][y2]==-1:
            return float("-inf")
        key = (x1,y1,x2,y2)
        if key in check:
            return check[key]
        if x1==x2 and y1==y2:
            cherry = grid[x1][y1]
        else:
            cherry = grid[x1][y1]+grid[x2][y2]
            
        res = cherry +max(self.helper(grid,n,x1+1,y1,x2+1,y2,check),
            self.helper(grid,n,x1+1,y1,x2,y2+1,check),
            self.helper(grid,n,x1,y1+1,x2,y2+1,check),
            self.helper(grid,n,x1,y1+1,x2+1,y2,check)
        )    
        
        check[key]=res
        
        return res
        
        
        
        