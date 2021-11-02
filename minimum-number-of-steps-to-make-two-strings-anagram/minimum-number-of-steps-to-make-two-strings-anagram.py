class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dic=defaultdict(int)
        for i in s:
            dic[i]+=1
        count=0    
        for c in t:
            if dic[c]!=0:
                dic[c]-=1
            else:
                count+=1
        return count        
        #return sum(dic.values())        