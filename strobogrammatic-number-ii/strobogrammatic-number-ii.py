class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        
        evenMidCandidate = ["11","69","88","96", "00"]
        oddMidCandidate = ["0", "1", "8"]
        if n == 1:
            return oddMidCandidate
        if n == 2:
            return evenMidCandidate[:-1]
        if n % 2:
            pre, midCandidate = self.findStrobogrammatic(n-1), oddMidCandidate
        else: 
            pre, midCandidate = self.findStrobogrammatic(n-2), evenMidCandidate
        premid = (n-1)//2
        return [p[:premid] + c + p[premid:] for c in midCandidate for p in pre]
    
#         check = {"1":"1","6":"9","8":"8","9":"6","0":"0"}
#         arr=["1","0","6","9","8"]
#         res = []
#         path1 = []
#         path2=[]
        
#         self.helper(n,check,res,path1,path2,arr)
#         return res
    
#     def helper(self,n,check,res,path1,path2,arr):
#         if n==0:
#             if len(path1)>1:
               
#                 if path1[0]!="0" and "".join(reversed(path1)) =="".join(path2):
                
#                     res.append("".join(path1))
#             elif len(path1)==1:
       
#                 if "".join(reversed(path1)) =="".join(path2):
                
#                     res.append("".join(path1))
#             return 
#         for i in arr:
#             self.helper(n-1,check,res,path1+[i],path2+[check[i]],arr)
            
            