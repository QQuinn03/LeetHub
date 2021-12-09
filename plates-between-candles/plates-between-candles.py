class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n=len(s)
        before=[0]*n
        can=0
        if s[0]=="*":
            can=None
        if s[0]=="|":
            can=0
        
        for i in range(1,len(s)):
            if s[i]=="|":
                if can is not None:
                    before[i]=before[i-1]+can
                can=0
            else:
                before[i]=before[i-1]
                if can is not None:
                    can+=1
        print(before)            
        after=[0]*n
        
        if s[-1]=="*":
            can=None
        if s[-1]=="|":
            can =0
        for i in range(n-2,-1,-1):
            if s[i]=="|":
                if can!=None:
                    after[i]=after[i+1]+can
                can=0
            else:
                after[i]=after[i+1]
                if can!=None:
                    can+=1
        total=max(after)
        
        res=[]
        for i in queries:
            left=i[0]
            right=i[1]
            val=max(0,after[left]+before[right]-total)
            res.append(val)
        return res     
            