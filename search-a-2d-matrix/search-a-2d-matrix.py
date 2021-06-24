class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1
        
        while l<=r:
            mid = (l+r)//2
            if matrix[mid][0]<=target and target<=matrix[mid][-1]:
                left = 0
                right = len(matrix[0])-1
                while left<=right:
                    m = (left+right)//2
                    if matrix[mid][m]==target:
                        return True
                    elif matrix[mid][m]<target:
                        left = m+1
                    else:
                        right = m-1
                return False
            elif matrix[mid][0]<target and matrix[mid][-1]<target:
                l = mid+1
            else:
                r = mid-1
        
        return False
        
        
                