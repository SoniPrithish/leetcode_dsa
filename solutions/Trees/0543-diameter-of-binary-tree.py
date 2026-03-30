# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxd=0
        def solve(root):
            nonlocal maxd
            if root is None:
                return 0
            
            left = solve(root.left)
            right = solve(root.right)
            maxd = max(maxd, left + right)
            return max(left, right) + 1
        solve(root)
        return maxd
