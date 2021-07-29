class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        check = [chr(i) for i in range(ord('A'),ord('Z')+1)]
        res = []
        
        while columnNumber>0:
            temp = (columnNumber-1)%26
       
            res.append(check[temp])
            columnNumber= (columnNumber-1)//26
        
        return "".join(reversed(res))