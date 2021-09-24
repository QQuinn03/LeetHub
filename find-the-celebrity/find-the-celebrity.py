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
        self.n=n
        for i in range(n):
            if self.helper(i)==1:
                return i
        return -1
    
    def helper(self,i):
        for j in range(self.n):
            if i ==j:
                continue
            if knows(i,j) or not knows(j,i):
                return False
        return True    
            