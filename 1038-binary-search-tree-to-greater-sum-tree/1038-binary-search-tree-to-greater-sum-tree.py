# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode | None) -> TreeNode | None:
        total = [0]

        def dfs(node):
            if node is None:
                return

            # Visit larger values first
            dfs(node.right)

            # Add current value to running sum
            total[0] += node.val
            node.val = total[0]

            # Then visit smaller values
            dfs(node.left)

        dfs(root)
        return root