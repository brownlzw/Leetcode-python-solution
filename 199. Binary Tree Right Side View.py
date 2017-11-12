# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def rightSideView(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res = []
    self.dfs(res, root, 0)
    return res

  def dfs(self, res, root, d):
    if not root:
      return
    if d == len(res):
      res.append(root.val)
    self.dfs(res, root.right, d + 1)
    self.dfs(res, root.left, d + 1)