# You are given an integer array nums. The unique elements of an array are the
# elements that appear exactly once in the array.

# Return the sum of all the unique elements of nums.


# Example 1:

# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: 0
# Explanation: There are no unique elements, and the sum is 0.
# Example 3:

# Input: nums = [1,2,3,4,5]
# Output: 15
# Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.

from collections import defaultdict


class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        """Calculates the sum of all elements that appear exactly once in the array.

        This method uses a hash map to count the frequency of each element.
        It first iterates through the input list to populate the frequency map.
        Then, it iterates through the map to sum up keys that have a value of 1.

        Args:
            nums: A list of integers.

        Returns:
            The sum of unique elements. Returns 0 if no unique elements exist.

        Time Complexity:
            O(N) where N is the number of elements in `nums`.
            We iterate through `nums` once (O(N)) and then through the unique
            keys in `frequencies` once (at most O(N)). Dictionary operations are O(1).

        Space Complexity:
            O(N) in the worst case to store the frequency dictionary,
            where all elements in `nums` are unique.
        """

        frequencies = defaultdict(int)
        ans = 0

        for num in nums:
            frequencies[num] += 1

        for key, val in frequencies.items():
            if val == 1:
                ans += key

        return ans
