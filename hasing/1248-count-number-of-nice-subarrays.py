# Given an array of integers nums and an integer k. A continuous subarray is
# called nice if there are k odd numbers on it.

# Return the number of nice sub-arrays.


# Example 1:

# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
# Example 2:

# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There are no odd numbers in the array.
# Example 3:

# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16

from collections import defaultdict


class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        answer = current = 0

        for num in nums:
            current += num % 2
            answer += counts[current - k]
            counts[current] += 1

        return answer


# Complexity Analysis
# Time complexity: O(n), where n is the length of the input array nums. We
# traverse the array once.
# Space complexity: O(n) in the worst case, where all numbers in nums are odd.
# In this case, we would store n + 1 different counts in the hashmap.
