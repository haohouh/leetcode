class Trie:
    def __init__(self):
        self.root = {}
        self.isEnd = -1


    def insert(self,word):
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur[self.isEnd] = True

    def search(self,word):
        cur = self.root
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        
        if self.isEnd not in cur:
            return False
        return True
    
    def prefix(self,word):
        cur = self.root
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return True

if __name__ == "__main__":
    a = Trie()
    a.insert("abc")
    a.insert("abd")
    a.insert("ef")
    print(a.root)
    print(a.prefix("abe"))