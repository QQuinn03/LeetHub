class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1=m-1
        idx2=n-1
        
        for i in range(m+n-1,-1,-1):
            if idx2<0:
                break     
            
            if idx1>=0 and nums1[idx1]>=nums2[idx2]:   
                nums1[i]=nums1[idx1]
                idx1-=1
            elif nums1[idx1]<nums2[idx2] or idx2>=0:
                nums1[i]=nums2[idx2]
                idx2-=1    
        return nums1          
                
            
        