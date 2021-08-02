class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        res = []
        
        l = len(strs[0])
        for i in range(1,len(strs)):
            l = min(l,len(strs[i]))
            while strs[i][:l]!=strs[0][:l]:
                l-=1
            res.append(l)
        return strs[0][:min(res)] 