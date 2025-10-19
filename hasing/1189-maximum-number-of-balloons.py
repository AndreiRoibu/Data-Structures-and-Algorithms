# Given a string text, you want to use the characters of text to form
# as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum
# number of instances that can be formed.


# Example 1:


# Input: text = "nlaebolko"
# Output: 1
# Example 2:


# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0

from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = defaultdict(int)
        for char in text:
            counts[char] += 1

        return min(counts["b"], counts["a"], counts["n"], counts["l"] // 2, counts["o"] // 2)


# Complexity Analysis:
# Time Complexity: O(n), where n is the length of the input string text.
# We traverse the string once to count the occurrences of each character.
# Space Complexity: O(1), since the size of the counts dictionary is
# fixed and does not depend on the input size.
