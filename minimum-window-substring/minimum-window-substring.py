class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required={}
        count=0
        for i in t:
            if i not in required:
                required[i]=1
            else:
                required[i]+=1
        required_size=len(required)        
        res=(float("inf"),0,0)
        dic={}
        check=0
        right=0
        left=0
        
        while right<len(s):
            if s[right] not in dic:
                dic[s[right]]=1
            else:
                dic[s[right]]+=1
            if s[right]in required and dic[s[right]]==required[s[right]]:
                count+=1
            while count== required_size and left<=right:
                char = s[left]
                if right-left+1<res[0]:
                    res=(right-left+1,left,right)
                dic[char]-=1
                if char in required and dic[char]<required[char]:
                    count-=1
                left+=1    
            right+=1
        left=res[1]
        right=res[2]
        if res[0]==float("inf"):
            return ""
        return s[left:right+1]
                
            