class Trie:

    def __init__(self):
        self.root={}
        

    def insert(self, word: str) -> None:
        d=self.root

        for l in word:
            if l not in d:
                d[l]={}
            d=d[l]
        
        d['.']='.'

    def search(self, word: str) -> bool:
        
        d=self.root

        for l in word:
            if l not in d:
                return False
            d=d[l]
        
        return "." in d


    def startsWith(self, prefix: str) -> bool:
        d=self.root

        for l in prefix:
            if l not in d:
                return False
            d=d[l]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)