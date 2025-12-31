# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum
# average value and return this value. Any answer with a calculation error
# less than 10-5 will be accepted.

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000


# Constraints:

# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        sum_value = 0
        for i in range(k):
            sum_value += nums[i]

        answer = sum_value
        for i in range(k, len(nums)):
            sum_value += nums[i] - nums[i - k]
            answer = max(answer, sum_value)

        return answer / k


# Explanation:
# - Compute the sum of the first window of size k.
# - Slide the window by one each step, updating the sum in O(1).
# - Track the maximum window sum and divide by k at the end.

# Complexity Analysis:
# - Time complexity: O(N), where N is the length of nums. We traverse the nums
#   array once.
# - Space complexity: O(1). We use only a constant amount of extra space.
