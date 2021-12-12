# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(n):          
                if self.helper(i,n)==1:
                    return i
        return -1     
    
    def helper(self,i,n):
        for j in range(n):
            if i==j:
                continue
            if knows(i,j) or not knows(j,i):
                return 0
            
        return 1     
    
    