# Given an array of integers nums and an integer k, return the number of
# contiguous subarrays where the product of all the elements in the subarray
# is strictly less than k.

# Example 1:

# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Example 2:

# Input: nums = [1,2,3], k = 0
# Output: 0

# Constraints:

# 1 <= nums.length <= 3 * 104
# 1 <= nums[i] <= 1000
# 0 <= k <= 106


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        answer = left = 0
        current = 1

        for right in range(len(nums)):
            current *= nums[right]
            while current >= k:
                current /= nums[left]
                left += 1

            # We can consider every subarray that ends at right and begins at an
            # index between left and right as a valid window.
            # Locking in the ending point, we have right - left + 1 choices for
            # the starting point.
            answer += right - left + 1

        return answer


# Complexity Analysis:
# Time complexity: O(n), where n is the length of nums. Each element is
# processed at most twice (once by the right pointer and once by the left pointer).
# Space complexity: O(1), as we are using only a constant amount of extra space.
