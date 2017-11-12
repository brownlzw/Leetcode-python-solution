class Solution(object):
  def numDistinctIslands(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if not grid or not grid[0]:
      return 0
    nrow = len(grid)
    ncol = len(grid[0])
    islands = set()
    for i in xrange(nrow):
      for j in xrange(ncol):
        if grid[i][j] == 1:
          grid[i][j] = -1
          lst = [(i, j)]
          tups = [(0, 0)]
          while lst:
            lst1 = []
            for x, y in lst:
              if x > 0 and grid[x - 1][y] == 1:
                grid[x - 1][y] = -1
                lst1.append((x - 1, y))
                tups.append((x - 1 - i, y - j))
              if x < nrow - 1 and grid[x + 1][y] == 1:
                grid[x + 1][y] = -1
                lst1.append((x + 1, y))
                tups.append((x + 1 - i, y - j))
              if y > 0 and grid[x][y - 1] == 1:
                grid[x][y - 1] = -1
                lst1.append((x, y - 1))
                tups.append((x - i, y - 1 - j))
              if y < ncol - 1 and grid[x][y + 1] == 1:
                grid[x][y + 1] = -1
                lst1.append((x, y + 1))
                tups.append((x - i, y + 1 - j))

            lst = lst1
          tups.sort()
          islands.add(tuple(tups))
    return len(islands)
