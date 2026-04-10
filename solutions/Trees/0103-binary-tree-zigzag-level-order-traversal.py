# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        if not root:
            return []
        q=deque([root])
        ct=-1
        while(q):
            levelsize=len(q)
            level=[]
            ct+=1
            for _ in range(levelsize):
                data=q.popleft()
                level.append(data.val)
                if data.left:
                    q.append(data.left)
                if data.right:
                    q.append(data.right)
            if ct%2==0:
                result.append(level)
            else:
                result.append(level[::-1])
        return result
