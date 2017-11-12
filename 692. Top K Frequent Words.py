class Solution(object):
  def topKFrequent(self, words, k):
    """
    :type words: List[str]
    :type k: int
    :rtype: List[str]
    """
    m = {}
    for word in words:
      if word not in m:
        m[word] = 0
      else:
        m[word] += 1
    words = list(set(words))
    words.sort(key = lambda x: (-m[x], x))
    return words[:k]