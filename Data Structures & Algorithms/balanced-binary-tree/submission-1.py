# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
import math

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> list[bool, int]:
            if not node:
                return [True, 0]

            left, right = dfs(node.left), dfs(node.right)

            if math.fabs(left[1] - right[1]) <= 1 and left[0] and right[0]:
                return [True, max(left[1], right[1]) + 1]
            
            return [False, max(left[1], right[1]) + 1]

        return dfs(root)[0]