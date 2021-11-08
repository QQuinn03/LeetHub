from collections import deque
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        
        que=deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="*":
                    que.append((i,j,1))
                    break
        
        visited=set()
        while que:
            x,y,z = que.popleft()
      
            # visited.add((x,y))
            for i in [(0,-1),(0,1),(1,0),(-1,0)]:
                new_x=x+i[0]
                new_y=y+i[1]
                if 0<=new_x<m and 0<=new_y<n and grid[new_x][new_y]!="X":
                   
                    if grid[new_x][new_y]=="#":
                   
                        return z
                    elif grid[new_x][new_y]=="O": 
                       
                        que.append((new_x,new_y,z+1))
                        grid[new_x][new_y]="X"
        return -1
        
                        
                    
            
        