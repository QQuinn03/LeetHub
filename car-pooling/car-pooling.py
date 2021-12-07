class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        times=[]
        for i in trips:
            times.append([i[1],i[0]])
            times.append([i[2],-i[0]])
        times.sort()
        total=0
        for i in times:
            total+=i[1]
            if total>capacity:
                return False
        return True    