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
            if s[right] not in dic:
                res = max(res,right-left+1)
            else:
                if dic[s[right]]>=left:
                    left = dic[s[right]]+1
                    
                else:
                    res=max(res,right-left+1)
            dic[s[right]]=right
            right+=1
        return res     