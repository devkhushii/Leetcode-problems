# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:

        def search(inorder, left, right, val):
            for i in range(left, right + 1):
                if inorder[i] == val:
                    return i

        preIdx = [0]

        def build(preorder, inorder, preIdx, left, right):
            if left > right:
                return None

            root = TreeNode(preorder[preIdx[0]])

            index = search(
                inorder,
                left,
                right,
                preorder[preIdx[0]]
            )

            preIdx[0] += 1

            root.left = build(
                preorder,
                inorder,
                preIdx,
                left,
                index - 1
            )

            root.right = build(
                preorder,
                inorder,
                preIdx,
                index + 1,
                right
            )

            return root

        return build(preorder, inorder, preIdx, 0, len(inorder) - 1)