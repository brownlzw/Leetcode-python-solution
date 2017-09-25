class Solution(object):
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid or not grid[0]:
      return 0
    count = 0
    r, c = len(grid), len(grid[0])
    for i in xrange(r):
      for j in xrange(c):
        if grid[i][j] == '1':
          count += 1
          self.dfs(i, j, grid)
    return count

  def dfs(self, r, c, grid):
    a = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    if grid[r][c] == '1':
      grid[r][c] = "2"
      for i, j in a:
        print i, j
        rr, cc = r + i, c + j
        if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]) and grid[rr][cc] != '2':
          self.dfs(rr, cc, grid)
