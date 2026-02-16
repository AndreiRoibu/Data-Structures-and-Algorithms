# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.


# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:

# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:

# Input: nums = [1,2,3]
# Output: 0


# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100

# Hint 1
# Count how many times each number appears. If a number appears n times,
# then n * (n - 1) // 2 good pairs can be made with this number.

from collections import Counter, defaultdict


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        """Calculates the number of 'good' pairs (i, j) where nums[i] == nums[j] and i < j.

        This approach uses combinatorics to count pairs efficiently.
        Instead of iterating through all pairs (O(N^2)), we count the frequency of each number.
        For a number appearing `n` times, the number of ways to choose 2 indices is given by
        the combination formula C(n, 2) = n * (n - 1) / 2.

        Mathematical Insight:
        - If a number appears `k` times, any two distinct indices form a valid pair.
        - The number of pairs is the sum of integers from 1 to k-1.
        - This is equivalent to the arithmetic series sum: k * (k - 1) // 2.

        Args:
            nums: A list of integers.

        Returns:
            The total count of good pairs.

        Time Complexity:
            O(N), where N is the length of `nums`.
            - Building the frequency map (Counter) takes O(N).
            - Iterating through the unique keys in the map takes O(K), where K is the number of
              unique elements (K <= N).
            - The calculations inside the loop are O(1).
            - Total time is dominated by the initial pass: O(N).

        Space Complexity:
            O(N) (specifically O(K)) to store the frequency counts in the hash map.
            In the worst case (all elements unique), K = N.
        """
        # 1. Count frequency of each number: O(N)
        counter = Counter(nums)
        ans = 0

        # 2. Apply combinatorial formula for each number: O(K)
        # Formula: nC2 = n * (n-1) / 2
        for count in counter.values():
            if count > 1:
                ans += count * (count - 1) // 2

        return ans


# Can this be further improved?
# Algorithmically: No. You must inspect every element at least once, so O(N)
# time is optimal.
# Space: O(N) space is required to store counts. We could sort the array first
# to do it in O(1) space (excluding sort stack) but that would raise time
# complexity to O(N log N).

# Alternative One-Pass Approach:
# We can actually compute the answer in a single pass while building the counts.


# As we iterate, if we see a number that has appeared k times before, it forms
# k new pairs with the previous instances. Then we increment the count.
class Solution2:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = defaultdict(int)
        ans = 0
        for num in nums:
            # Current num forms a pair with all previous instances of num
            ans += count[num]
            count[num] += 1
        return ans


# This avoids the second loop and the division, potentially slightly faster,
# but same asymptotic complexity. Your current solution is perfectly fine and
# mathematically elegant.
