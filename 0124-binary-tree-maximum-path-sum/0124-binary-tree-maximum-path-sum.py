# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maxSum=[float('-inf')]

        def dfs(root):
            if root is None:
                return 0
            left_gain=max(0,dfs(root.left))
            right_gain=max(0,dfs(root.right))
            current=left_gain+right_gain+root.val

            maxSum[0]=max(maxSum[0],current)
            return root.val + max(left_gain, right_gain)

        dfs(root)

        return maxSum[0]


        