import string
from collections import defaultdict
class Solution(object):
  def findLadders(self, beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: List[List[str]]
    """
    def dfs(res, li, path, beginWord, endWord):
      if beginWord == endWord:
        res.append(li)
        return
      if beginWord not in path:
        return
      for word in path[beginWord]:
        dfs(res, li + [word], path, word, endWord)

    wordList = set(wordList)
    if not wordList or endWord not in wordList:
      return []
    forward, backward = {beginWord}, {endWord}
    path = defaultdict(list)
    flag = True
    found = False
    while forward and backward and not found:
      cur, other = forward, backward
      if len(forward) > len(backward):
        cur, other = backward, forward
        flag = False
      next = set()
      for word in cur:
        for i in xrange(len(word)):
          first, second = word[:i], word[i + 1:]
          for c in string.ascii_lowercase:
            temp = first + c + second
            if temp in other:
              if flag:
                path[word].append(temp)
              else:
                path[temp].append(word)
              found = True
              continue
            if temp in wordList:
              if flag:
                path[word].append(temp)
              else:
                path[temp].append(word)
              next.add(temp)
      if flag:
        forward = next
      else:
        backward = next
    res = []
    dfs(res, [], path, beginWord, endWord)
    return res
