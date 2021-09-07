from collections import defaultdict
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        idx1 = -len(wordsDict)
        idx2=len(wordsDict)
        res = float("inf")
        for idx,val in enumerate(wordsDict):
            if wordsDict[idx]==word1:
                if wordsDict[idx]==word2:
                    idx2=idx1
                idx1=idx
            elif wordsDict[idx]==word2:
                if wordsDict[idx]==word1:
                    idx1=idx2
                idx2=idx
            res = min(res,abs(idx1-idx2))
        return res    