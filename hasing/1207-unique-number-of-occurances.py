# Given an array of integers arr, return true if the number of occurrences of
# each value in the array is unique or false otherwise.


# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values
# have the same number of occurrences.
# Example 2:

# Input: arr = [1,2]
# Output: false
# Example 3:

# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true


# Constraints:

# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000

# Hint 1
# Find the number of occurrences of each element in the array using a hash map.
# Hint 2
# Iterate through the hash map and check if there is a repeated value.

from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        """Determines if the number of occurrences of each value in the array is unique.

        The method counts the frequency of each element using a hash map.
        It then compares the number of unique frequencies to the number of unique elements.
        If they match, it implies every element has a distinct frequency count.

        Args:
            arr: A list of integers.

        Returns:
            True if the number of occurrences of each value is unique, False otherwise.

        Time Complexity:
            O(N) where N is the length of `arr`.
            - Iterating through `arr` to build the counter takes O(N).
            - Creating sets from keys and values takes O(K), where K is the number of unique elements (K <= N).
            - Overall complexity is linear.

        Space Complexity:
            O(N) in the worst case to store the frequency dictionary and the sets.
            - The dictionary stores up to N unique keys.
            - The sets store up to N unique counts/keys.
        """
        counter = defaultdict(int)
        for value in arr:
            counter[value] += 1
        return len(set(counter.values())) == len(counter)
