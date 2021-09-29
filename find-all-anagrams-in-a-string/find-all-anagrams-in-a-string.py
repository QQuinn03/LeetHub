class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s)<len(p):
            return []
            
        s_arr= [0]*26
        res=[]
        check = [0]*26
        for i in p:
            check[ord(i)-ord("a")]+=1
        
        for i in range(len(p)):
            s_arr[ord(s[i])-ord("a")]+=1
        
        if s_arr==check:
            res.append(0)
        
        right = len(p)
        left=0
        for i in range(right,len(s)):
            s_arr[ord(s[left])-ord("a")]-=1
            s_arr[ord(s[i])-ord("a")]+=1
            if s_arr==check:
                res.append(left+1)
            left+=1
        return res    
        
        
            