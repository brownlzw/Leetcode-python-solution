# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def widthOfBinaryTree(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    res = []
    self.dfs(res, root, 0, 0)
    return max([pos[1] - pos[0] + 1 for pos in res])

  def dfs(self, res, root, d, pos):
    if not root:
      return
    if d == len(res):
      res.append([pos, pos])
    else:
      if pos < res[d][0]:
        res[d][0] = pos
      elif pos > res[d][1]:
        res[d][1] = pos
    self.dfs(res, root.left, d + 1, 2 * pos + 1)
    self.dfs(res, root.right, d + 1, 2 * pos + 2)
