class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        
        for i in range(5,n+1,5):
            val = i
            while val%5==0:
                count+=1
                val = val//5
        return count        