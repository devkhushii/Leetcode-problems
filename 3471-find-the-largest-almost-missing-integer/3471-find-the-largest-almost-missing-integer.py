class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        f = {}
        for num in nums:
            f[num] = f.get(num, 0) + 1

        # Every element forms its own window
        if k == 1:
            ans = -1

            for num in nums:
                if f[num] == 1:
                    ans = max(ans, num)

            return ans

        # Only one window: the entire array
        if k == n:
            return max(nums)

        # 1 < k < n
        ans = -1

        if f[nums[0]] == 1:
            ans = max(ans, nums[0])

        if f[nums[-1]] == 1:
            ans = max(ans, nums[-1])

        return ans