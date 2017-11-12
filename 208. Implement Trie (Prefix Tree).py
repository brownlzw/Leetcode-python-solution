class Trie(object):
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.trie = {}

  def insert(self, word):
    """
    Inserts a word into the trie.
    :type word: str
    :rtype: void
    """
    curr = self.trie
    for w in word:
      if w not in curr:
        curr[w] = {}
      curr = curr[w]
    curr["EOW"] = True

  def search(self, word):
    """
    Returns if the word is in the trie.
    :type word: str
    :rtype: bool
    """
    curr = self.trie
    for w in word:
      if w not in curr:
        return False
      curr = curr[w]

    return "EOW" in curr

  def startsWith(self, prefix):
    """
    Returns if there is any word in the trie that starts with the given prefix.
    :type prefix: str
    :rtype: bool
    """
    curr = self.trie
    for w in prefix:
      if w not in curr:
        return False
      curr = curr[w]

    return True