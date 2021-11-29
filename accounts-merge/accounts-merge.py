from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph=defaultdict(set)
        email_name={}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[email].add(account[1])
                graph[account[1]].add(email)
                email_name[email]=name
        
        res=[]
        seen=set()
        for email in email_name:
            if email not in seen:
                que=[email]
                seen.add(email)
                sub=[email]
                while que:
                    node=que.pop(0)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            que.append(nei)
                            sub.append(nei)
                res.append([email_name[email]]+sorted(sub))
            
        return res      
              
                        
                
                
        
        
        
        
            
            
        
        