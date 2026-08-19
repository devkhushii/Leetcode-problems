class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = {}

        for row, seat in reservedSeats:
            if row not in reserved:
                reserved[row] = set()

            reserved[row].add(seat)

        ans = (n - len(reserved)) * 2

        for seats in reserved.values():

            left = not any(x in seats for x in [2, 3, 4, 5])
            right = not any(x in seats for x in [6, 7, 8, 9])
            middle = not any(x in seats for x in [4, 5, 6, 7])

            if left and right:
                ans += 2
            elif left or right or middle:
                ans += 1

        return ans