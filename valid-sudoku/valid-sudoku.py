class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = len(board)
        col = len(board[0])
        
        
        for i in range(row):
            dic={}
            for j in range(col):
                if board[i][j]!=".":
                    if board[i][j] in dic:
                        print("h1",board[i][j])
                        return False
                    dic[board[i][j]]=0
        
        for i in range(col):
            dic={}
            for j in range(row):
                if board[j][i]!=".":
                    if board[j][i] in dic:
                        print("h2")
                        return False
                    dic[board[j][i]]=0
        
        row_ = [0,3,6]
        col_=[0,3,6]
        
        for i in row_:
            for j in col_:
                dic = {}
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        if board[x][y]!=".":
                            if board[x][y] in dic:
                              
                                return False
                            dic[board[x][y]]=0
        return True                     
                    
        
     