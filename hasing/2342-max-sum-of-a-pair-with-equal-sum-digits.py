# You are given a 0-indexed array nums consisting of positive integers. You can
# choose two indices i and j, such that i != j, and the sum of digits of the
#  number nums[i] is equal to that of nums[j].

# Return the maximum value of nums[i] + nums[j] that you can obtain over all
# possible indices i and j that satisfy the conditions. If no such pair of
# indices exists, return -1.


# Example 1:

# Input: nums = [18,43,36,13,7]
# Output: 54
# Explanation: The pairs (i, j) that satisfy the conditions are:
# - (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
# - (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
# So the maximum sum that we can obtain is 54.
# Example 2:

# Input: nums = [10,12,19,14]
# Output: -1
# Explanation: There are no two numbers that satisfy the conditions, so we return -1.


# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109

from collections import defaultdict


class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        def get_digit_sum(num):
            digit_sum = 0
            while num:
                digit_sum += num % 10
                num //= 10
            return digit_sum

        dct = defaultdict(int)

        answer = -1

        for num in nums:
            digit_sum = get_digit_sum(num)
            if digit_sum in dct:
                answer = max(answer, num + dct[digit_sum])
            dct[digit_sum] = max(num, dct[digit_sum])

        return answer


# Explanation:
# - Compute the digit sum for each number.
# - Track the largest number seen for each digit sum.
# - When a digit sum repeats, update the best pair sum.

# Complexity Analysis:
# Time Complexity: O(N * D), where N is the number of elements in the input
# array nums, and D is the number of digits in the maximum number in nums. This is
# because we iterate through each element in nums (O(N)) and for each element, we
# calculate the sum of its digits (O(D)).
# Space Complexity: O(K), where K is the number of unique digit sums encountered.
# In the worst case, we may have to store an entry in the dictionary for each
# element in nums, leading to O(N) space complexity.
