class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        dic = {}
        left=0
        right = 0
        res=0
        
        while right<len(s):
            dic[s[right]]=right
            if len(dic)>2:
                val = min(dic.values())
                left = val+1
                del dic[s[val]]
            res=max(res,right-left+1)  
            right+=1
        return res    
            