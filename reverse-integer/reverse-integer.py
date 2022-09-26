class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        
        res=0
        count = 0
        flag=1
        
        if x<0:
            flag=-1
            x*=-1
            
        while x!=0:
            digit = x%10
            x=x//10
            res=res*10+digit
            
        if flag==-1:
            res*=-1
        if res>2**31-1 or res<-2**31-1:
            return 0
        return res
            