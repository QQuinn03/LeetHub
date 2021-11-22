class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        
        while left<right:
            if s[left]!=s[right]:
                return self.helper(s,left+1,right) or self.helper(s,left,right-1)
            
            else:
                left+=1
                right-=1
        return True         

    def helper(self,s,l,r):
        while l<=r:
            if s[l]!=s[r]:
                return False
                
            l+=1
            r-=1
        return True   
            
