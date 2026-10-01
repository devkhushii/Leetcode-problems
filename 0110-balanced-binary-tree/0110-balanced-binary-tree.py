# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
      

        def helper(root):
            if root is None:
                return 0,True
            left_height, left_balanced = helper(root.left)
            right_height, right_balanced = helper(root.right)
            balanced = (
                        left_balanced and
                        right_balanced and
                        abs(left_height - right_height) <= 1
                    )
            current_height=1+max(left_height,right_height)

           
            return current_height,balanced

        height,balanced=helper(root)
        return balanced
        