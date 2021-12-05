class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        check=[0]+flowerbed+[0]
        total=0
        
        for i in range(1,len(check)-1):
            if check[i]==0:
                if check[i-1]!=1 and check[i+1]!=1:
                    check[i]=1
                    total+=1
        return total>=n            
                    