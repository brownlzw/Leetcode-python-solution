class Solution(object):
  def fullJustify(self, words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    res, cur = [], []
    count = 0
    for word in words:
      if count + len(cur) + len(word) > maxWidth:
        intervals= len(cur) - 1 or 1
        for i in xrange(maxWidth - count):
          cur[i % intervals] += ' '
        res.append(''.join(cur))
        cur = []
        count = 0
      cur.append(word)
      count += len(word)
    last = [' '.join(cur) + ' ' * (maxWidth - count - len(cur) + 1)]
    return res + last