class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.v = vec
        self.row=0
        self.col=0
       
        

    def next(self) -> int:
        if self.hasNext():
            val=self.v[self.row][self.col]
            self.col+=1
            return val
        else:
            return
        
    def hasNext(self) -> bool:
        while self.row<len(self.v):
            if self.col<len(self.v[self.row]):
                return True
            self.row+=1
            self.col=0
        return False     
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()