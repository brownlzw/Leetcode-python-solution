class Solution(object):
  def totalNQueens(self, n):
    """
    :type n: int
    :rtype: int
    """
    mask = (1 << n) - 1
    self.count = 0
    self.dfs(0, 0, 0, mask)
    return self.count

  def dfs(self, l, r, col, mask):
    if col == mask:
      self.count += 1
      return
    pos = mask & (~(l | r | col))
    while pos:
      p = pos & -pos
      pos &= pos - 1
      self.dfs((l | p) << 1, (r | p) >> 1, col | p, mask)
