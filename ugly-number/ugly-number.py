class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n ==0:
            return 0
        for p in [2,3,5]:
            while n%p==0:
                n=n//p
        if n ==1:
            return True
        return False
                
            
            