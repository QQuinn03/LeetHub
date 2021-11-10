class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
      
        n = len(grid)
        que=deque([])
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    que.append((i,j,0))
        distance=0
        visited=set()
        
        while que:
        
            x,y,d=que.popleft()
            #visited.add((x,y))

            distance=max(distance,d)


            for i in [(0,1),(0,-1),(1,0),(-1,0)]:
                new_x=i[0]+x
                new_y=i[1]+y
                if new_x>=0 and new_x<n and new_y>=0 and new_y<n:

                        if grid[new_x][new_y]==0:
                            grid[new_x][new_y]=1
                            que.append((new_x,new_y,d+1))
        return distance or -1                
            
        