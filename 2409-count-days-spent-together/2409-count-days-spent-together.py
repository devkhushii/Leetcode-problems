class Solution:
    def countDaysTogether(
        self,
        arriveAlice: str,
        leaveAlice: str,
        arriveBob: str,
        leaveBob: str
    ) -> int:

        days = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]

        def toDay(date):
            month = int(date[:2])
            day = int(date[3:])

            return sum(days[:month - 1]) + day

        alice_start = toDay(arriveAlice)
        alice_end = toDay(leaveAlice)

        bob_start = toDay(arriveBob)
        bob_end = toDay(leaveBob)

        start = max(alice_start, bob_start)
        end = min(alice_end, bob_end)

        return max(0, end - start + 1)