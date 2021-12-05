class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic={}
        self.list=[]
    
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dic:
            return False
        self.list.append(val)
        self.dic[val]=len(self.list)-1
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dic:
            return False
        else:
            idx=self.dic[val]
            value=self.list[-1]
            self.list[idx]=value
            
            self.dic[value]=idx
            del self.dic[val]
            self.list.pop()
            return True
        return False
        
       

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()