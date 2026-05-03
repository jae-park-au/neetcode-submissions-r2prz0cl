# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia = 0

        def helper(node: Optional[TreeNode]) -> int:
            nonlocal max_dia

            if not node:
                return 0

            left, right = helper(node.left), helper(node.right)

            max_dia = max(max_dia, left + right)

            return max(left, right) + 1

        helper(root)

        return max_dia

            