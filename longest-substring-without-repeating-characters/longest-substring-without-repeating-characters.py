class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        left = 0
        right = 0
        res = 0
        
        while right<len(s):
            if s[right] in dic:
                if left <=dic[s[right]]:
                    left = dic[s[right]]+1
            dic[s[right]]=right
                    
            res= max(res,right-left+1)
            right+=1
            
            
        return res    
                