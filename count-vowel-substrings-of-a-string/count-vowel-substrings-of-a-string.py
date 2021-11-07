class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        check=set("aeiou")
        res=0
        for i in range(len(word)):
            pattern=set()
            for j in range(i,len(word)):
                if word[j] not in check:
                    break
                pattern.add(word[j])
                res+=int(len(pattern)==5)
        return res    