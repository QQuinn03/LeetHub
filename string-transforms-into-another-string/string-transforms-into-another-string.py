class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        dic={}
        idx=0
        
        while idx<len(str1):
            if str1[idx] not in dic:
                dic[str1[idx]]=str2[idx]
            if dic[str1[idx]]!= str2[idx]:
                print(dic[str1[idx]],str2[idx])
                return False
            idx+=1
        return str1 == str2 or len(set(str2)) < 26  