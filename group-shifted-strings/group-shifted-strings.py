class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dic = {}
        for i in strings:
            diff = ()
            for j in range(1,len(i)):
                key = (ord(i[j])-ord(i[j-1]))%26
                diff+=(key,)
            print(diff)    
            if diff not in dic:
                dic[diff]=[i]
            else:
                dic[diff].append(i)
        res=[]        
        for val in dic.values():
            res.append(val)
        return res    
        
        