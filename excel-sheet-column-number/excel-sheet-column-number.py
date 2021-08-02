class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        dic = {}
        for i in range(26):
            dic[chr(i+65)]=i+1
        n = len(columnTitle)
        for i in range(n):
            chr_val = columnTitle[n-1-i]
            res +=(dic[chr_val]*(26**i))
   
        return res    