class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            temp = "".join(sorted(i))
     
            if temp in dic:
                dic[temp].append(i)
            else:
                dic[temp]=[i]
     
        res=[]
        for i,val in dic.items():
            res.append(val)
        return res    
                
            