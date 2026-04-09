# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def t(n):
            if n.val == 1:
                return True
            elif n.val == 0:
                return False
            else:
                if n.val == 2:
                    return t(n.left) or t(n.right)
                if n.val == 3:
                    return t(n.left) and t(n.right)
        return t(root)