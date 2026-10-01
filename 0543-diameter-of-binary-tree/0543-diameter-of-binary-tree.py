class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        ans = [0]

        def height(node):
            if not node:
                return 0

            lh = height(node.left)
            rh = height(node.right)

            ans[0] = max(ans[0], lh + rh)

            return 1 + max(lh, rh)

        height(root)
        return ans[0]