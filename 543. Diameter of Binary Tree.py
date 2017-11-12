# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            self.max_len = max(self.max_len, left + right + 2)
            return max(left, right) + 1

        self.max_len = 0
        dfs(root)
        return self.max_len
    # like 124, O(n), O(logn)