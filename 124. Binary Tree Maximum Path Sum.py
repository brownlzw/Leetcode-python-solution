# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            if not node:
                return 0
            res = node.val
            left = dfs(node.left)
            if left > 0:
                res += left
            right = dfs(node.right)
            if right > 0:
                res += right
            if res > max_sum[0]:
                max_sum[0] = res
            return max(left, right, 0) + node.val

        max_sum = [-float('inf')]
        dfs(root)
        return max_sum[0]
    # O(n), O(logn, n)