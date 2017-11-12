# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        st = []
        for num in nums:
            node = TreeNode(num)
            while st and num > st[-1].val:
                node.left = st.pop()
            if st:
                st[-1].right = node
            st.append(node)
        return st[0]
    # O(n)

        if not nums:
            return None
        root, maxi = TreeNode(max(nums)), nums.index(max(nums))
        root.left = self.constructMaximumBinaryTree(nums[:maxi])
        root.right = self.constructMaximumBinaryTree(nums[maxi + 1:])
        return root
    # O(h * n)