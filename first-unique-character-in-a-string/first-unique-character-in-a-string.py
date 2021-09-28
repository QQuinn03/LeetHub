class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]]=i
            else:
                dic[s[i]]+=len(s)
        res = len(s)
        
        for i in dic:
            if dic[i]<res:
                res=dic[i]
        if res== len(s):
            return -1
        return res