class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        right = 0
        dic = {}
        res = 0
        
        while right<len(s):
            dic[s[right]]=right
            if len(dic)>k:
                key = min(dic.values())
                left=key+1
                del dic[s[key]]
            res = max(res,right-left+1)
            right+=1
        return res     