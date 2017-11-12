# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
      if not root:
        return
      q = [root]
      while q:
        frontier = []
        prev = None
        for node in q:
          if prev:
            prev.next = node
          if node.left:
            frontier.append(node.left)
          if node.right:
            frontier.append(node.right)
          prev = node
        q = frontier
