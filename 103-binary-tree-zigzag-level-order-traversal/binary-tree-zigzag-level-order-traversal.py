# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        resdict=defaultdict(list)

        def traversal(root,height):
            if not root:
                return
            
            height+=1
            resdict[height].append(root.val)

            traversal(root.left,height)
            traversal(root.right,height)

            return resdict

        traversal(root,0)
        res=[]
        if resdict:
            for key,val in sorted(resdict.items()):
                if key%2==0:
                    val.reverse()
                res.append(val)
        return res