# Given an array of integers arr, a lucky integer is an integer that has a
# frequency in the array equal to its value.

# Return the largest lucky integer in the array. If there is no lucky integer
# return -1.


# Example 1:

# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:

# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
# Example 3:

# Input: arr = [2,2,2,3,3]
# Output: -1
# Explanation: There are no lucky numbers in the array.


# Constraints:

# 1 <= arr.length <= 500
# 1 <= arr[i] <= 500

from collections import defaultdict


class Solution:
    def findLucky(self, arr: list[int]) -> int:
        """Finds the largest 'lucky' integer in the array.

        A lucky integer is an integer that has a frequency in the array
        equal to its value. This method counts the frequency of each element
        using a hash map, then iterates through the unique elements to find the
        maximum integer where the key equals its frequency.

        Args:
            arr: A list of integers.

        Returns:
            The largest lucky integer, or -1 if none exists.

        Time Complexity:
            O(N), where N is the length of `arr`.
            Iterating through the array to build the counter takes O(N).
            Iterating through the dictionary items takes at most O(N) (number of
                unique elements).

        Space Complexity:
            O(N) to store the counts of unique elements in the dictionary.
        """
        counter = defaultdict(int)
        ans = -1
        for elem in arr:
            counter[elem] += 1
        for key, value in counter.items():
            if key == value:
                ans = max(ans, key)
        return ans
