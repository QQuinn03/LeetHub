class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        seen=set()
        seen.add("")
        res=""
        print(words)
        for word in words:
            
            if word[:-1] in seen:
               
                if len(res)<len(word): 
                    res=word
                seen.add(word)
        return res              
      