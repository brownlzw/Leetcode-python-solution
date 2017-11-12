# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def convertBST(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    def dfs(root):
      if not root:
        return
      dfs(root.right)
      self.bigsum += root.val
      root.val = self.bigsum
      dfs(root.left)

    self.bigsum = 0
    dfs(root)
    return root
