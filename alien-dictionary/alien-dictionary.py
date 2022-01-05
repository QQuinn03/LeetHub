from collections import defaultdict, Counter, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        adj_list=defaultdict(set)
        in_degree={}
        for word in words:
            for char in word:
                if char not in in_degree:
                    in_degree[char]=0

        
        for i in range(1,len(words)):
            word1=words[i-1]
            word2=words[i]
            
            size1=len(word1)
            size2=len(word2)
            size=min(size1,size2)
            flag=0
            for j in range(size):
         
                if word1[j]!=word2[j]:
                    if word2[j] not in adj_list[word1[j]]:
                        adj_list[word1[j]].add(word2[j])
                        in_degree[word2[j]]+=1
                      
                    break
            else: 
                if len(word1)>len(word2):
                     
                        return ""
                    
                    
                
        print(adj_list)  
        print(in_degree)
        
        res = []
        que = deque([])
        for i in in_degree:
            if in_degree[i]==0:
                que.append(i)
        
        while que:
            node = que.popleft()
            res.append(node)
            for d in adj_list[node]:
                in_degree[d]-=1
                if in_degree[d]==0:
                    #print("0",d,in_degree[d])
                    que.append(d)
        
                
        if len(res) < len(in_degree):
     
            return ""
        return "".join(res)
