class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1={}
        dic2={}
        
        for i in nums1:
            if i not in dic1:
                dic1[i]=[i]
            else:
                dic1[i].append(i)
        for i in nums2:
            if i not in dic2:
                dic2[i]=[i]
            else:
                dic2[i].append(i)
        
        res=[]
        for i in dic1:
            if i in dic2:
                res+=min(dic1[i],dic2[i])
        return res        
            
                