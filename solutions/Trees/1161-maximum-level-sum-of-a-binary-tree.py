# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sum=[]
        def dfs(node,level):
            if not node:
                return
            if level == len(level_sum):
                level_sum.append(0)
            
            level_sum[level] += node.val

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root,0)
        return level_sum.index(max(level_sum)) + 1
