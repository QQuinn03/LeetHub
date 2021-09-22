class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        for i in range(len(s)):
            temp = self.helper(s,i,i)
            if len(res)<len(temp):
                res=temp
            temp = self.helper(s,i,i+1)
            if len(res)<len(temp):
                res=temp
        return res
    
    def helper(self,s,i,j):
        while i>-1 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
        return s[i+1:j]        
            
            
        