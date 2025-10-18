# Given a string s, return true if s is a good string, or false otherwise.

# A string s is good if all the characters that appear in s have
# the same number of occurrences (i.e., the same frequency).


# Example 1:

# Input: s = "abacbc"
# Output: true
# Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
# Example 2:

# Input: s = "aaabb"
# Output: false
# Explanation: The characters that appear in s are 'a' and 'b'.
# 'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.


# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters.

from collections import defaultdict


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        return len(set(counts.values())) == 1


# Complexity Analysis
# Time complexity: O(n), where n is the length of the string s. We traverse the
# string once to count the occurrences of each character and then again to check
# if all counts are the same.
# Space complexity: O(1), since the number of distinct characters is limited to 26
# (lowercase English letters). Alternatively, we can say O(k), where k is the number of
# distinct characters in the string s.
