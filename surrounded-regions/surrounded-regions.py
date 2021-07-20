class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        
        for i in range(row):
            self.helper(board,i,0,row,col)
            self.helper(board,i,col-1,row,col)
        for j in range(col):
            self.helper(board,0,j,row,col)
            self.helper(board,row-1,j,row,col)
        
        for i in range(row):
            for j in range(col):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="G":
                    board[i][j]="O"
        return board            
    
    def helper(self,board,i,j,row,col):
        if i<0 or i>=row or j<0 or j >=col or board[i][j]!="O":
            return 
        board[i][j]="G"
        self.helper(board,i+1,j,row,col)
        self.helper(board,i-1,j,row,col)
        self.helper(board,i,j+1,row,col)
        self.helper(board,i,j-1,row,col) 
                