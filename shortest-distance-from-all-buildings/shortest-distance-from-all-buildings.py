class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        hits=[[0 for i in range(col)] for j in range(row)]
        distance=[[0 for i in range(col)] for j in range(row)]
        count=0
        buildings=0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    buildings+=1
                    
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    seen=set()
                    if self.bfs(grid,seen,i,j,hits,distance,count,buildings)==-1:
                        return -1
        print(distance)            
        res=float("inf")
        for i in range(row):
            for j in range(col):
                if distance[i][j]<res and grid[i][j]!=1 and hits[i][j]==buildings:
                    
                    res=distance[i][j]
        if res==float("inf"):
            return -1
        return res
    
    def bfs(self,grid,seen,i,j,hits,distance,count,buildings):
        que=deque([(i,j,0)])
        while que:
            x,y,z=que.popleft()
            for i in [(-1,0),(0,-1),(1,0),(0,1)]:
                new_x=x+i[0]
                new_y=y+i[1]
                if 0<=new_x<len(grid) and 0<=new_y<len(grid[0]) and (new_x,new_y) not in seen:
                    seen.add((new_x,new_y))
                    if grid[new_x][new_y]==0:
                        distance[new_x][new_y]+=z+1
                        hits[new_x][new_y]+=1
                        que.append((new_x,new_y,z+1))
                    elif grid[new_x][new_y]==1:
                        count+=1
        return count==buildings              