# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter=0

    def caldep(self,node:Optional[TreeNode])-> int:

        l=self.caldep(node.left) if node.left else 0
        r=self.caldep(node.right) if node.right else 0
        self.diameter=max(self.diameter,l+r)

        return 1+max(l,r)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.caldep(root)
        return self.diameter

        