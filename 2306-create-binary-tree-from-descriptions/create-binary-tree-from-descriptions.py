# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        a = {}
        b = set()
        for thing in descriptions:
            b.add(thing[1])
            if thing[0] not in a:
                a[thing[0]] = TreeNode(thing[0])
            if thing[1] not in a:
                a[thing[1]] = TreeNode(thing[1])
            if thing[2] == 0:
                a[thing[0]].right = a[thing[1]]
                continue
            a[thing[0]].left = a[thing[1]]
        for thing in a.keys():
            if thing not in b:
                return a[thing]
        