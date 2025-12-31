# Given an array of integers nums and an integer k, return the total number of
# subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.


# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2


# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107


from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        answer = current = 0

        for num in nums:
            current += num
            answer += counts[current - k]
            counts[current] += 1

        return answer


# Explanation:
# - Track prefix sums and how often each sum has occurred.
# - A subarray sums to k when current_sum - k has been seen before.
# - Accumulate counts of such prefixes as we scan.

# Complexity Analysis
# Time complexity: O(n), where n is the length of the input array nums. We
# traverse the array once, performing constant-time operations for each element.
# Space complexity: O(n) in the worst case, when all prefix sums are distinct.
