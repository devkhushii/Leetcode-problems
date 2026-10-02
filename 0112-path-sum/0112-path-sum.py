# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:

        def helper(root,targetSum,currentSum):
            if root is None:
                return False
            
            currentSum+=root.val
            if root.left is None and root.right is None:
                if currentSum==targetSum:
                    return True
                return False
            return (
                    helper(root.left, targetSum, currentSum)
                    or helper(root.right, targetSum, currentSum)
                )

        return helper(root,targetSum,0)
        