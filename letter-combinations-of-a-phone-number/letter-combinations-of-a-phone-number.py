class Solution(object):
    def __init__(self):
        self.dic = {"2":["a","b","c"], 
                   "3":["d","e","f"],
                   "4":["g","h","i"],
                   "5":["j","k","l"],
                   "6":["m","n","o"],
                   "7":["p","q","r","s"], 
                   "8":["t","u","v"],
                   "9":["w","x","y","z"]} 
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=="":
            return []
        res=[]
        size=len(digits)
        combine=""
        self.helper(digits,res,size,combine)
        return res
    
    def helper(self,digits,res,size,combine):
        if len(combine)==size:
            res.append(combine)
            return 
        for i in range(len(digits)):
            for char in self.dic[digits[i]]:
                self.helper(digits[i+1:],res,size,combine+char)
        
        