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
        if len(digits)==0:
            return digits
        res = []
        self.helper(digits,"",res,len(digits))
        return res
    
    def helper(self,digits,path,res,size):
        if len(path)==size:
            res.append(path)
            return
        for i in range(len(digits)):
            for c in self.dic[digits[i]]:
                self.helper(digits[i+1:],path+c,res,size)
            
            
            
  
 
