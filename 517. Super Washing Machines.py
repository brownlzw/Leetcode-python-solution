class Solution(object):
  def findMinMoves(self, machines):
    """
    :type machines: List[int]
    :rtype: int
    """
    s = sum(machines)
    if not machines or s % len(machines):
      return -1
    avg = s / len(machines)
    cnt = 0
    res = 0
    for num in machines:
      cnt += num - avg
      res = max(res, abs(cnt), num - avg)
    return res
