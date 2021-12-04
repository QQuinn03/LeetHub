class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required={}
        for char in t:
            if char not in required:
                required[char]=1
            else:
                required[char]+=1
        required_length=len(required)
        
        check={}
        left=0
        right=0
        res=(float("inf"),left,right)
        count=0
        
        while right<len(s):
            if s[right] not in check:
                check[s[right]]=1
            else:
                check[s[right]]+=1
                
            if s[right] in required and check[s[right]]==required[s[right]]:
                count+=1
                
            while count== required_length and left<=right:
                char=s[left]
                
                if right-left+1<res[0]:
                    res=(right-left+1,left,right)
                    
                check[char]-=1
                if char in required and check[char]<required[char]:
                    count-=1
                left+=1
                
            right+=1
            
        if res[0]==float("inf"):
            return ""
        left=res[1]
        right=res[2]
        return s[left:right+1]
                
        
                
        
                
            