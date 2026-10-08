import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        max_value = float('-inf')

        # Put first element of every list into heap
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            max_value = max(max_value, nums[i][0])

        best_left = heap[0][0]
        best_right = max_value

        while True:
            min_value, list_index, element_index = heapq.heappop(heap)

            # Current range
            if max_value - min_value < best_right - best_left:
                best_left = min_value
                best_right = max_value

            # Move to next element in the same list
            next_index = element_index + 1

            # If this list has no more elements,
            # we can no longer cover every list
            if next_index == len(nums[list_index]):
                break

            next_value = nums[list_index][next_index]

            heapq.heappush(
                heap,
                (next_value, list_index, next_index)
            )

            max_value = max(max_value, next_value)

        return [best_left, best_right]