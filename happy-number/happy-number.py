class Solution:
    def isHappy(self, n: int) -> bool:
        dic = {}
        while n!=1:
            n = self.helper(n)
            if n in dic:
                return False
            else:
                dic[n]=0
        return True
    
    def helper(self,n):
        res = 0
        while n!=0:
            reminder = n%10
            n = n//10
            res +=reminder**2
        return res     
            