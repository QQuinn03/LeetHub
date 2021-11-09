class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words=sorted(words,key=lambda x:len(x))
        dic = {word:1 for word in words}
        
        for word in words:
            for i in range(len(word)):
                cur = word[:i]+word[i+1:]
                if cur in dic:
                    dic[word]=max(dic[word],dic[cur]+1)
        return max(dic.values())             
            
            
            