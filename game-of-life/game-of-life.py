class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        """
        row=len(board)
        col = len(board[0])
        copy = [[0 for i in range(col)]for j in range(row)]
        
        for i in range(row):
            for j in range(col):
                copy[i][j]=board[i][j]
  
        neighbors=[(-1,-1),(-1,0),(-1,1),(0,1),(0,-1),(1,1),(1,0),(1,-1)]
        
        for i in range(row):
            for j in range(col):
                live_nei = 0
                for nei in neighbors:
                    r = (i+nei[0])
                    c = (j+nei[1])
                    
                    if (r<row and r>=0) and (c<col and c>=0)and(copy[r][c]==1):
                   
                        live_nei+=1
                if copy[i][j]==1 and(live_nei<2 or live_nei>3):
                  
                    board[i][j]=0
                if copy[i][j]==0 and live_nei==3:
                
                    board[i][j]=1
                    
                        