# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.pre = None
        def traversal(cur: TreeNode) ->bool:                
            if not cur:
                return True

            if not traversal(cur.left):
                return False
            if self.pre and cur.val <= self.pre.val:    
                return False
            self.pre = cur
            
            return traversal(cur.right)
        
        return traversal(root)

            