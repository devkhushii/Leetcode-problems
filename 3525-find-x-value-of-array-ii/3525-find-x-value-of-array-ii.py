class Node:
    def __init__(self, k):
        self.prod = 1
        self.cnt = [0] * k


class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        self.tree = [Node(k) for _ in range(4 * self.n)]
        self.build(1, 0, self.n - 1, nums)

    def merge(self, left, right):
        node = Node(self.k)

        # Product of the complete segment
        node.prod = (left.prod * right.prod) % self.k

        # Prefixes completely inside left
        for r in range(self.k):
            node.cnt[r] += left.cnt[r]

        # Prefixes that continue into right
        for r in range(self.k):
            new_r = (left.prod * r) % self.k
            node.cnt[new_r] += right.cnt[r]

        return node

    def build(self, idx, left, right, nums):
        if left == right:
            value = nums[left] % self.k
            self.tree[idx].prod = value
            self.tree[idx].cnt[value] = 1
            return

        mid = (left + right) // 2

        self.build(idx * 2, left, mid, nums)
        self.build(idx * 2 + 1, mid + 1, right, nums)

        self.tree[idx] = self.merge(
            self.tree[idx * 2],
            self.tree[idx * 2 + 1]
        )

    def update(self, idx, left, right, pos, value):
        if left == right:
            value %= self.k

            self.tree[idx].prod = value
            self.tree[idx].cnt = [0] * self.k
            self.tree[idx].cnt[value] = 1
            return

        mid = (left + right) // 2

        if pos <= mid:
            self.update(idx * 2, left, mid, pos, value)
        else:
            self.update(idx * 2 + 1, mid + 1, right, pos, value)

        self.tree[idx] = self.merge(
            self.tree[idx * 2],
            self.tree[idx * 2 + 1]
        )

    def query(self, idx, left, right, ql, qr):
        if ql <= left and right <= qr:
            return self.tree[idx]

        mid = (left + right) // 2

        if qr <= mid:
            return self.query(idx * 2, left, mid, ql, qr)

        if ql > mid:
            return self.query(idx * 2 + 1, mid + 1, right, ql, qr)

        left_node = self.query(idx * 2, left, mid, ql, qr)
        right_node = self.query(idx * 2 + 1, mid + 1, right, ql, qr)

        return self.merge(left_node, right_node)


class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        tree = SegmentTree(nums, k)
        answer = []

        for index, value, start, x in queries:

            # Permanent update
            tree.update(1, 0, n - 1, index, value)

            # Query nums[start ... n-1]
            node = tree.query(1, 0, n - 1, start, n - 1)

            answer.append(node.cnt[x])

        return answer