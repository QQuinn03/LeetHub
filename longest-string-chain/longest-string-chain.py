class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=lambda x:len(x))
        print(words)
        dp={word:1 for word in words}
        
        for word in words:
            for j in range(len(word)):
                temp=word[:j]+word[j+1:]
                if temp in dp:
                    dp[word]=max(dp[word],dp[temp]+1)
        return max(dp.values())          
                