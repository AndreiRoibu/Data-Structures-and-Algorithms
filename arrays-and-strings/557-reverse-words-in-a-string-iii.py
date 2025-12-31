# Given a string s, reverse the order of characters in each word within a
# sentence while still preserving whitespace and initial word order.


# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "Mr Ding"
# Output: "rM gniD"


# Constraints:

# 1 <= s.length <= 5 * 104
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.


class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        start = 0
        len_chars = len(chars)

        for i in range(len_chars + 1):
            if i == len_chars or chars[i] == " ":
                left, right = start, i - 1
                while left < right:
                    chars[left], chars[right] = chars[right], chars[left]
                    left += 1
                    right -= 1
                start = i + 1

        return "".join(chars)


# Explanation:
# - Convert the string to a list so we can swap characters in place.
# - Scan for word boundaries (spaces or end), then reverse that segment.
# - Join the list back into a string with words reversed in place.

# Complexity Analysis:
# Time complexity: O(n), where n is the length of s. We traverse the list of characters
# once, and each character is involved in at most one swap.
# Space complexity: O(n), since we convert the string to a list of characters
# which takes additional space proportional to the size of the input string.
