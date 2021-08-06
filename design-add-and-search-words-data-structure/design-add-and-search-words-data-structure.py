class TrieNode(object):
    def __init__(self):
        self.child ={}
        self.is_word = False
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for i in word:
            if i not in cur.child:
                new = TrieNode()
                cur.child[i]=new
            cur = cur.child[i]
        cur.is_word = True          
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.root
        return self.helper(cur,word)
    
    def helper(self,root,word):
        if word =="":
            return root.is_word
        cur = root
    
        
        for i in range(len(word)):
            char = word[i]
            if word[i]!=".":
                if char not in cur.child:
                    return False
                cur = cur.child[char]
            else:
                for nxt in cur.child.values():
                   
                    if self.helper(nxt,word[i+1:])==True:
                        return True
                return False
        return cur.is_word        
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)