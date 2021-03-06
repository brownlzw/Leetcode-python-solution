# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def is_same(s, t):
            if not s or not t:
                return not s and not t
            return s.val == t.val and is_same(s.left, t.left) and is_same(s.right, t.right)

        if not s or not t:
            return not s and not t
        if is_same(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(self.right, t)
    # O(mn)
    # O(m + n) serialize both tree and see substring