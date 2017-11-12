class Solution(object):
  def leastBricks(self, wall):
    """
    :type wall: List[List[int]]
    :rtype: int
    """
    if not wall or not wall[0]:
      return 0
    m = {}
    max_count = 0
    for row in wall:
      total = 0
      for i in xrange(len(row) - 1):
        total += row[i]
        if total not in m:
          m[total] = 1
        else:
          m[total] += 1
        max_count = max(max_count, m[total])
    return len(wall) - max_count
