# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        result=[]
        def preorder(node):

            if not node:
                result.append(10**5)
                return
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(p)
        strA=result
        result=[]
        preorder(q)
        strB=result
        
        return strA==strB
