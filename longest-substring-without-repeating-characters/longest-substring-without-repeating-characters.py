class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        right=0
        dic={}
        res=0
        
        while right<len(s):
            if s[right] not in dic:
                dic[s[right]]=right
                res=max(res,right-left+1)
            else:
                if left<=dic[s[right]]:
                    left=dic[s[right]]+1
                else:
                    res=max(res,right-left+1)
                dic[s[right]]=right
            right+=1
        return res    
         
                    
            