# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:

        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        qque=deque([q])
        pque=deque([p])
        while qque and pque:
            qsize=len(qque)
            psize=len(pque)
            plevel=[]
            qlevel=[]
            if qsize!=psize:
                return False
            for _ in range(psize):
                pnode=pque.popleft()
                qnode=qque.popleft()
                if pnode.val!=qnode.val:
                    return False
                plevel.append(pnode.val)
                qlevel.append(qnode.val)
                if (pnode.left is None) != (qnode.left is None):
                    return False
                if pnode.left and qnode.left:
                    qque.append(qnode.left)
                    pque.append(pnode.left)
                if (pnode.right is None) != (qnode.right is None):
                    return False
                if pnode.right and qnode.right:
                    qque.append(qnode.right)
                    pque.append(pnode.right)
        return True
        