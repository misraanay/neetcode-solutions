class TrieNode:
    def __init__(self):
        self.word = False
        self.children =  {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.word = True

    def search(self, word: str) -> bool:
        cur = self.root
        def find(i, cur):
            if i == len(word):
                return cur.word
            if word[i] != '.':
                if word[i] not in cur.children:
                    return False
                return find(i+1, cur.children[word[i]])
            for key in cur.children:
                if find(i+1, cur.children[key]):
                    return True
            return False
        return find(0, cur)
