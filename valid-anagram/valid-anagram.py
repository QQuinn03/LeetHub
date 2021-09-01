class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in s:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        dic1 = {}
        for i in t:
            
            if i not in dic1:
                dic1[i]=1
            else:
                dic1[i]+=1
                
        if dic1!=dic:
            return False
        return True
            