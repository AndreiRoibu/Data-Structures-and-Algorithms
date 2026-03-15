# Given two strings s and p, return an array of all the start indices of p's
# anagrams in s. You may return the answer in any order.


# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".


# Constraints:

# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.

from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        """Finds all starting indices of p's anagrams in s.

        This solution uses a Fixed-Size Sliding Window with Hash Maps (dictionaries).
        Since an anagram of p must have the exact same length and character counts
        as p, we create a window in s of length len(p). We slide this window across
        s one character at a time, updating the character frequencies and comparing
        them to the target frequencies of p. If they match, we record the start index.

        Args:
            s (str): The string we are searching within.
            p (str): The target string (we are looking for its anagrams).

        Returns:
            List[int]: A list of starting indices of the anagrams in s.

        Time Complexity:
            O(S + P): Where S is the length of `s` and P is the length of `p`.
            Building the initial dictionaries takes O(P) time. Sliding the window
            takes O(S - P) time. Comparing two dictionaries of size at most 26
            (lowercase English letters) takes O(1) time. Total time is strictly linear.

        Space Complexity:
            O(1) auxiliary space (excluding the output array `ans`).
            The dictionaries `p_dict` and `freq` store character counts. Since
            the strings only consist of lowercase English letters, the dictionaries
            will hold a maximum of 26 key-value pairs. This means the memory used
            is constant, regardless of how large the input strings are.
        """
        # Array to store the starting indices of valid anagrams
        ans = []

        s_len = len(s)
        p_len = len(p)

        # If the target string is longer than the search string, no anagrams can exist
        if p_len > s_len:
            return ans

        # p_dict acts as our "target recipe" to compare against
        p_dict = defaultdict(int)

        # freq acts as our "current basket" of characters in the sliding window
        freq = defaultdict(int)

        # 1. Build a fixed window and populate both dictionaries for the first `p_len` characters
        left = 0
        for right in range(p_len):
            p_dict[p[right]] += 1
            freq[s[right]] += 1

        # Check if the very first window is already an anagram
        if p_dict == freq:
            ans.append(0)

        # 2. Slide the window one character at a time through the rest of s
        for right in range(p_len, s_len):
            # Add the new character entering the window from the right
            freq[s[right]] += 1

            # Remove the oldest character leaving the window from the left
            freq[s[left]] -= 1

            # If a character's count drops to 0, completely delete it from the dictionary.
            # This is critical! Python dictionary equality `==` checks keys as well.
            # `{'a': 1, 'b': 0}` does NOT equal `{'a': 1}`.
            if freq[s[left]] == 0:
                del freq[s[left]]

            # Move the left pointer forward to maintain the fixed window size
            left += 1  # noqa: SIM113

            # Compare our current window's frequency map to our target map.
            # If they match exactly, we found an anagram starting at 'left'.
            if p_dict == freq:
                ans.append(left)

        return ans
