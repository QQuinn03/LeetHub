class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        dic = {}
        for i in range(len(s)):
            temp = s[i:i+10]
            if temp not in dic:
                dic[temp]=1
            else:
                res.add(temp)
        return res        
            
        