# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def tree2str(self, t):
    """
    :type t: TreeNode
    :rtype: str
    """
    if not t:
      return ""
    res = str(t.val)
    if not t.left and not t.right:
      return res
    l = self.tree2str(t.left)
    res += "(" + l + ")"
    r = self.tree2str(t.right)
    if r:
      res += "(" + r + ")"
    return res

