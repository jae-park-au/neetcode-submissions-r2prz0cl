# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = deque()
        stack.append(root)

        while stack:
            cur_node = stack.pop()

            if self.subtreeHelper(cur_node, subRoot):
                return True

            if cur_node.left is not None:
                stack.append(cur_node.left)
            if cur_node.right is not None:
                stack.append(cur_node.right)

        return False

    def subtreeHelper(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if root and subRoot and root.val == subRoot.val:
            return self.subtreeHelper(root.left, subRoot.left) and self.subtreeHelper(root.right, subRoot.right)
        else:
            return False
