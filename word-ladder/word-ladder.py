from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph= defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                node = word[:i]+"_"+word[i+1:]
                graph[node].add(word)
        que = deque([])
        que.append((beginWord,1))
        seen = set()
        while que:
            word,step = que.popleft()
            if word == endWord:
                return step
            seen.add(word)
            for i in range(len(word)):
                node = word[:i]+"_"+word[i+1:]
                if node in graph:
                    for check_word in graph[node]:
                        if check_word not in seen:
                            seen.add(check_word)
                            que.append((check_word,step+1))
        return 0                    
            
                
                
        