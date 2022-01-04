class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        arr=list(num)
   
        path=""
        res=[]

        idx=0
        self.helper(arr,idx,path,res,target)
        return res
    
    def helper(self,arr,idx,path,res,target):
        if idx>=len(arr):
            return 
        if idx==len(arr)-1:
            
            path=path+arr[idx]
            if eval(path)==target:
          
                res.append(path)
                return 
  
        self.helper(arr,idx+1,path+arr[idx]+"+",res,target)
        self.helper(arr,idx+1,path+arr[idx]+"*",res,target)
        self.helper(arr,idx+1,path+arr[idx]+"-",res,target)
        if (path and path[-1] not in ["-","+","*"] and arr[idx]=="0") or arr[idx]!="0":
           
            self.helper(arr,idx+1,path+arr[idx],res,target)
            
        
        
                
            
        