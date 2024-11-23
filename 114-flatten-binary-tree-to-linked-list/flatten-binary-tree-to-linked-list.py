# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def createlink(root):
            if not root:
                return None
            
            left=createlink(root.left)
            right=createlink(root.right)

            if left:
                trav=left
                while trav.right:
                    trav=trav.right
                trav.right=right
            
                root.right=left
                root.left=None

            return root

        createlink(root)
        

        