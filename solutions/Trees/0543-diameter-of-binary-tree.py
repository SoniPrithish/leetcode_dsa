# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxd=0
        def solve(node):
            if not node:
                return 0
            nonlocal maxd
            left=solve(node.left)
            right=solve(node.right)

            maxd=max(maxd,left+right)

            return 1+max(left,right)
        solve(root)
        return maxd
