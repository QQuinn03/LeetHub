class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        graph=defaultdict(set)
        size=len(words)
        words.sort(key=lambda x:len(x))
        
        for i in range(size):
            word=words[i]
            for j in range(len(word)):
                graph[word[:j]+word[j+1:]].add(i)
        print(graph)        
        
        dis=[1]*size
        ans=1
        for i in range(size):
            for nei in graph[words[i]]:
                dis[nei]=max(dis[nei],dis[i]+1)
                ans=max(ans,dis[nei])
        return ans         