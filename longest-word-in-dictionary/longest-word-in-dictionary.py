class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        print(words)
        seen=set()
        seen.add("")
        res=""
        for word in words:
            if word[:-1] in seen:
                if len(word)>len(res):
                    res=word
                seen.add(word)
       
        return res       
            