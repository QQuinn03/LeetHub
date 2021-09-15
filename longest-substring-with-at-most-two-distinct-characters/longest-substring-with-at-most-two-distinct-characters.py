class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        right = 0
        left = 0
        res = 0
        
        while right<len(s):
            dic[s[right]]=right
            if len(dic)>2:
                val = min(dic.values())
                left = val+1
                del dic[s[val]]
            res = max(res,right-left+1) 
            
            right+=1
        return res    
                
                
           
            