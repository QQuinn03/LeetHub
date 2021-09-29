class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for i in strs:
            temp = "".join(sorted(i))
            if temp in dic:
                dic[temp].append(i)
            else:
                dic[temp]=[i]
        
        res = []
        for key,val in dic.items():
            res.append(val)
        
        return res