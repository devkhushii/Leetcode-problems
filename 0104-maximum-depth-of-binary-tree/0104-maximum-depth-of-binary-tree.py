# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        
        def helper(root):
            if root is None:
                return 0
            
            left = helper(root.left)
            right = helper(root.right)

            return 1 + max(left, right)
        return helper(root)


            

        