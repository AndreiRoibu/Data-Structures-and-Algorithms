# You are given an array nums consisting of positive integers.

# Return the total frequencies of elements in nums such that those elements all
# have the maximum frequency.

# The frequency of an element is the number of occurrences of that element in
# the array.


# Example 1:

# Input: nums = [1,2,2,3,1,4]
# Output: 4
# Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum
# frequency in the array.
# So the number of elements in the array with maximum frequency is 4.
# Example 2:

# Input: nums = [1,2,3,4,5]
# Output: 5
# Explanation: All elements of the array have a frequency of 1 which is the
# maximum.
# So the number of elements in the array with maximum frequency is 5.


# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100

# Hint 1
# Find frequencies of all elements of the array.
# Hint 2
# Find the elements that have the maximum frequencies and count their total occurrences.


from collections import defaultdict


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        """Calculates the total number of elements that have the maximum
        frequency.

        This method first counts the frequency of each element using a hash map.
        It then identifies the maximum frequency present in the map. Finally,
        it sums up the frequencies of all elements that appear exactly
            `max_frequency` times.

        Args:
            nums: A list of integers.

        Returns:
            The total count of elements with maximum frequency.

        Time Complexity:
            O(N) where N is the length of `nums`.
            - Building the frequency map takes O(N).
            - Finding `max_frequency` iterates over the unique keys, taking O(N)
                in worst case.
            - The final loop also iterates over the keys, taking O(N).
            - Total time is linear.

        Space Complexity:
            O(N) to store the frequency map.
            In the worst case (all elements unique), the map stores N entries.
        """

        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

        max_frequency = max(counter.values())

        return sum(value for value in counter.values() if value == max_frequency)


# Space Optimized Version:

# The problem constraints state 1 <= nums[i] <= 100.

# Instead of a dictionary, use a fixed-size array counts = [0] * 101.
# This reduces space complexity to O(1) (constant space relative to input size N,
#  since size is fixed at 101).
# It also avoids hashing overhead, making it faster in practice.


class Solution2:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        counts = [0] * 101
        max_freq = 0

        # Build frequency array and track max_freq simultaneously
        for num in nums:
            counts[num] += 1
            if counts[num] > max_freq:
                max_freq = counts[num]

        # Calculate sum
        ans = 0
        for freq in counts:
            if freq == max_freq:
                ans += freq

        return ans
