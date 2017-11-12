# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def checkEqualTree(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    m = set()
    count = [0]
    total = self.dfs(m, root, count)
    if not total:
      return count[0] > 1
    return (total & 1) == 0 and (total >> 1) in m

  def dfs(self, m, root, count):
    if not root:
      return 0
    left = self.dfs(m, root.left, count)
    right = self.dfs(m, root.right, count)
    cur = left + right + root.val
    if not cur:
      count[0] += 1
    m.add(cur)
    return cur