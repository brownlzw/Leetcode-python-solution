class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = set()
        self.trie = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.words.add(word)
        cur = self.trie
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur['$'] = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def search_trie(word, cur):
            if not cur:
                return False
            if not word:
                return '$' in cur
            for i, char in enumerate(word):
                if char == '.':
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if j in cur and search_trie(word[i + 1:], cur[j]):
                            return True
                    return False
                if char not in cur:
                    return False
                cur = cur[char]
            return '$' in cur

        if word in self.words:
            return True
        elif '.' not in word:
            return False
        else:
            return search_trie(word, self.trie)

        # Your WordDictionary object will be instantiated and called as such:
        # obj = WordDictionary()
        # obj.addWord(word)
        # param_2 = obj.search(word)

    # O(26 ^ i * l), O(sum(len))
    # O(N * l), O(sum(len))