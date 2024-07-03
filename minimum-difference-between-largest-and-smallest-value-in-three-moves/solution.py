class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 5:
            return 0
        nums.sort()
        @cache
        def getMinDiff(left, right, steps):
            if steps == 0:
                return nums[right] - nums[left]
            return min(getMinDiff(left + 1, right, steps - 1), getMinDiff(left, right - 1, steps - 1))
        return getMinDiff(0, n - 1, 3)