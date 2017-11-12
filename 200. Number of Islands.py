class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # promise root[i] == i
        if not grid or not grid[0]:
            return 0
        root = []
        count = 0
        m, n = len(grid), len(grid[0])
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1':
                    flag = True
                    if i > 0 and grid[i - 1][j] != '0':
                        grid[i][j] = root[grid[i - 1][j]]
                        flag = False
                    if j > 0 and grid[i][j - 1] != '0':
                        if flag:
                            grid[i][j] = root[grid[i][j - 1]]
                        else:
                            root[grid[i][j - 1]] = grid[i][j]
                        flag = False
                    if flag:
                        grid[i][j] = count
                        root.append(count)
                        count += 1
        return sum(root[i] == i for i in xrange(len(root)))

        O(mn), O(n)

        #   if not grid or not grid[0]:
        #     return 0
        #   count = 0
        #   r, c = len(grid), len(grid[0])
        #   for i in xrange(r):
        #     for j in xrange(c):
        #       if grid[i][j] == '1':
        #         count += 1
        #         self.dfs(i, j, grid)
        #   return count
        #
        # def dfs(self, r, c, grid):
        #   a = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        #   if grid[r][c] == '1':
        #     grid[r][c] = "2"
        #     for i, j in a:
        #       rr, cc = r + i, c + j
        #       if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]) and grid[rr][cc] != '2':
        #         self.dfs(rr, cc, grid)

    # O(mn), O(l)