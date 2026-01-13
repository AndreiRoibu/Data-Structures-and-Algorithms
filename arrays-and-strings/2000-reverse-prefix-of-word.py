# Given a 0-indexed string word and a character ch, reverse the segment of word
# that starts at index 0 and ends at the index of the first occurrence of ch
# (inclusive). If the character ch does not exist in word, do nothing.

# For example, if word = "abcdefd" and ch = "d", then you should reverse the
# segment that starts at 0 and ends at 3 (inclusive). The resulting string will
# be "dcbaefd".

# Return the resulting string.


# Example 1:

# Input: word = "abcdefd", ch = "d"
# Output: "dcbaefd"
# Explanation: The first occurrence of "d" is at index 3.
# Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".
# Example 2:

# Input: word = "xyxzxe", ch = "z"
# Output: "zxyxxe"
# Explanation: The first and only occurrence of "z" is at index 3.
# Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".
# Example 3:

# Input: word = "abcd", ch = "z"
# Output: "abcd"
# Explanation: "z" does not exist in word.
# You should not do any reverse operation, the resulting string is "abcd".


# Constraints:

# 1 <= word.length <= 250
# word consists of lowercase English letters.
# ch is a lowercase English letter.

# Hint 1
# Find the first index where ch appears.

# Hint 2
# Find a way to reverse a substring of word.


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        characters = list(word)
        left = right = 0

        if ch not in characters:
            return word

        while characters[right] != ch and right < len(characters):
            right += 1

        while left < right:
            characters[left], characters[right] = characters[right], characters[left]
            right -= 1
            left += 1

        return "".join(characters)


# Explanation:
# - Convert the string to a list of characters for easy manipulation.
# - Find the index of the first occurrence of ch.
# - Use two pointers to reverse the substring from the start to that index.
# - Join the list back into a string and return it.

# Complexity Analysis:
# Time complexity: O(n), where n is the length of the word. We may need to traverse
# the entire string to find ch and then reverse a portion of it.
# Space complexity: O(n), for storing the characters in a list.
