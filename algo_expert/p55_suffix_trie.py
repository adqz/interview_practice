class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.createSuffixTrie(i, string)

    def createSuffixTrie(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            char = string[j]
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.endSymbol] = True

    def contains(self, string):
        node = self.root
        # Traverse string
        for char in string:
            if char not in node:
                return False
            node = node[char]
        
        # Check if we've reached the end in the Trie
        if self.endSymbol in node:
            return True
        else:
            return False

