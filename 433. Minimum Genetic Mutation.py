import string
class Solution(object):
  def minMutation(self, start, end, bank):
    """
    :type start: str
    :type end: str
    :type bank: List[str]
    :rtype: int
    """
    bank = set(bank)
    if not bank or end not in bank:
      return -1
    forward, backward = {start}, {end}
    bank.discard(end)
    bank.discard(start)
    d = 0
    while forward and backward:
      if len(forward) > len(backward):
        forward, backward = backward, forward
      d += 1
      next = set()
      for word in forward:
        for i in xrange(len(word)):
          first, second = word[:i], word[i+1:]
          for c in "ACGT":
            cur = first + c + second
            if cur in backward:
              return d
            if cur in bank:
              next.add(cur)
              bank.discard(cur)
      forward = next
    return -1
