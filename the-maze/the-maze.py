class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        row=len(maze)
        col = len(maze[0])
        seen = set()
        dx=destination[0]
        dy=destination[1]
        x=start[0]
        y=start[1]
        
        if self.helper(x,y,row,col,seen,dx,dy,maze)==True:
            return True
        return False    
    
    def helper(self,x,y,row,col,seen,dx,dy,maze):

        if (x,y) in seen:
            return False
        seen.add((x,y))
        if (x,y)==(dx,dy):
          
            return True
        
        for i,j in [(0,-1),(0,1),(1,0),(-1,0)]:
            new_x=x
            new_y=y   
            
            while 0<=new_x+i<row and 0<=new_y+j<col and maze[new_x+i][new_y+j]!=1:
                new_x+=i
                new_y+=j
            if self.helper(new_x,new_y,row,col,seen,dx,dy,maze)==True:
                return True
                      
        return False        
                
        