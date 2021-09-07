class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        check = {"1":"1","6":"9","8":"8","9":"6","0":"0"}
        res=[]
        for i in reversed(num):
            if i not in check:
                return False
            res.append(check[i])
            
           
           
        return "".join(res)==num