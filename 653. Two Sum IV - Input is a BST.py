# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def findTarget(self, root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: bool
    """
    m = set()
    return self.dfs(root, m, k)

  def dfs(self, root, m, k):
    if not root:
      return False
    if k - root.val in m:
      return True
    m.add(root.val)
    return self.dfs(root.left, m, k) or self.dfs(root.right, m, k)