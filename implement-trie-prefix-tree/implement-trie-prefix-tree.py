class TrieNode(object):
    def __init__(self):
        self.child = {}
        self.is_word = False
        
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root= TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
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
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for i in word:
            if i not in cur.child:
                return False
            else:
                cur = cur.child[i]
        return cur.is_word    
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for i in prefix:
            if i not in cur.child:
                return False
                
            cur = cur.child[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)