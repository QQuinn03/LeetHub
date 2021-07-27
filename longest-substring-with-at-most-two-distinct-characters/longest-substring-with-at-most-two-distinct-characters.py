class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        dic = {}
        res = 0
        left = 0
        right = 0
        
        while right<len(s):
            dic[s[right]]=right
            if len(dic)>2:
                idx= min(dic.values())
                left= idx+1
                del dic[s[idx]]
                
            res = max(res,right-left+1)
            right+=1
        return res     
                