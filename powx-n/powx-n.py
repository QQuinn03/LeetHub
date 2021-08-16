class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n ==0:
            return 1
        if n >0:
            return self.helper(x,n)
        if n<0:
            return 1/self.helper(x,-n)
        
    def helper(self,x,n):
        if n ==0:
            return 1
        if x ==0:
            return 0
        if n %2 ==0:
            return self.helper(x*x,n//2)
        if n %2 == 1:
            return x *self.helper(x*x,n//2)
            
        
        