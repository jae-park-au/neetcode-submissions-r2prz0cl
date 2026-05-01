# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthHelper(root)

    def maxDepthHelper(self, node: Optional[TreeNode], cur_depth: int = 0) -> int:
        if not node:
            return cur_depth

        return max(self.maxDepthHelper(node.left, cur_depth + 1), self.maxDepthHelper(node.right, cur_depth + 1))