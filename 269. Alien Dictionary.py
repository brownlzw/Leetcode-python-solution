class Solution(object):
  def alienOrder(self, words):
    """
    :type words: List[str]
    :rtype: str
    """
    m = {}
    for word in words:
      for char in word:
        m[char] = set()
    for i in xrange(1, len(words)):
      for j in xrange(len(words[i])):
        if j < len(words[i - 1]) and words[i][j] != words[i - 1][j]:
          if words[i][j] not in m:
            m[words[i][j]] = set()
          m[words[i][j]].add(words[i - 1][j])
          break
    res = []
    cur = [key for key in m.keys() if not m[key]]
    while cur:
      res += cur
      for item in cur:
        del m[item]
        for key in m.keys():
          if item in m[key]:
            m[key].remove(item)
      cur = [key for key in m.keys() if not m[key]]
    if m:
      return ""
    return "".join(res)

    parents = defaultdict(list)
    indegree = {}
    for word in words:
      for c in word:
        indegree[c] = 0
    for word1, word2 in zip(words, words[1:]):
      for c1, c2 in zip(word1, word2):
        if c1 != c2:
          indegree[c2] += 1
          parents[c1].append(c2)
          break
    dq = deque()
    for c, v in indegree.items():
      if v == 0:
        dq.append(c)
    ret = []
    while dq:
      c = dq.popleft()
      ret.append(c)
      for child in parents[c]:
        indegree[child] -= 1
        if indegree[child] == 0:
          dq.append(child)
    return ''.join(ret) if len(ret) == len(indegree) else ''

