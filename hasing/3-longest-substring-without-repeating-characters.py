# Given a string s, find the length of the longest substring without duplicate characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and
# "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        answer = i = 0
        for idx in range(len(s)):
            if s[idx] in seen:
                i = max(seen[s[idx]], i)
            seen[s[idx]] = idx + 1
            answer = max(answer, idx + 1 - i)

        return answer


# Complexity Analysis:
# Time Complexity: O(N), where N is the length of the input string s. We
# traverse the string once.
# Space Complexity: O(M), where M is the size of the character set. In the
# worst case, we may store all characters in the dictionary. Because these
# are English letters, digits, symbols, and spaces, M is a constant, so we
# can consider the space complexity to be O(1).
