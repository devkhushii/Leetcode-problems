class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        if not head or not head.next or not head.next.next:
            return [-1, -1]

        idx = 2

        prev = head
        current = head.next
        nxt = head.next.next

        indices = []

        while nxt:
            if ((prev.val > current.val and nxt.val > current.val) or
                (prev.val < current.val and nxt.val < current.val)):
                indices.append(idx)

            idx += 1
            prev = current
            current = nxt
            nxt = nxt.next

        if len(indices) < 2:
            return [-1, -1]

        min_dis = float("inf")

        for i in range(1, len(indices)):
            min_dis = min(min_dis, indices[i] - indices[i - 1])

        max_dis = indices[-1] - indices[0]

        return [min_dis, max_dis]