# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        rows = binaryMatrix.dimensions()[0]
        cols = binaryMatrix.dimensions()[1]
       
        res=cols
        
        for row in range(rows):
            
            left=0
            right=cols-1
            while left<right:
                mid = left+(right-left)//2
                if binaryMatrix.get(row,mid)==0:
                    left=mid+1
                else:
                    right=mid 
            if binaryMatrix.get(row,left)==1:   
                res=min(res,left)
        if res==cols:
            return -1
        return res
            