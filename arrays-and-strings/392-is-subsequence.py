# 392. Is Subsequence
# Easy
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original
# string by deleting some (can be none) of the characters without disturbing the
# relative positions of the remaining characters. (i.e., "ace" is a subsequence
# of "abcde" while "aec" is not).


# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false


# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.


# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where
# k >= 10**9, and you want to check one by one to see if t has its subsequence.
# In this scenario, how would you change your code?


class Solution:  # pyright: ignore[reportRedeclaration]
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)


# Explanation:
# - Use two pointers to walk through s and t in order.
# - When characters match, advance the s pointer; always advance the t pointer.
# - If we consume all of s, then s is a subsequence of t.

# Complexity Analysis
# Time complexity: O(n), where n is the length of t. In the worst case, we
# might have to iterate through all characters of t.
# Space complexity: O(1), as we are using only a constant amount of extra space.

import bisect  # noqa: E402
from collections import defaultdict  # noqa: E402


class Solution:  # noqa: F811
    def isSubsequence(self, s: str, t: str) -> bool:
        pos = defaultdict(list)
        for i, ch in enumerate(t):
            pos[ch].append(i)

        # Walk through s using binary search
        prev = -1
        for ch in s:
            if ch not in pos:
                return False
            idx_list = pos[ch]
            j = bisect.bisect_right(idx_list, prev)  # next index > prev
            if j == len(idx_list):
                return False
            prev = idx_list[j]
        return True


# Explanation:
# - Precompute sorted index lists for each character in t.
# - For each character in s, binary search for the next index greater than the previous match.
# - If any character cannot be placed in order, s is not a subsequence.

# Complexity Analysis
# Time complexity: O(n + m log n), where n is the length of t and m is the length of s.
# Space complexity: O(n), as we are storing the indices of each character in t.
