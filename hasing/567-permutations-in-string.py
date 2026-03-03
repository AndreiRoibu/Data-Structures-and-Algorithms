# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.


# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false


# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.

# Hint 1
# Obviously, brute force will result in TLE. Think of something else.

# Hint 2
# How will you check whether one string is a permutation of another string?

# Hint 3
# One way is to sort the string and then compare. But, Is there a better way?

# Hint 4
# If one string is a permutation of another string then they must have one
# common metric. What is that?

# Hint 5
# Both strings must have same character frequencies, if one is permutation of
# another. Which data structure should be used to store frequencies?

# Hint 6
# What about hash table? An array of size 26?

from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Checks if a permutation of string s1 is a substring of string s2.

        This solution uses a Fixed-Size Sliding Window with Hash Maps (dictionaries).
        Since a permutation of s1 must have the exact same length and character counts
        as s1, we create a window in s2 of length len(s1). We then slide this window
        across s2 one character at a time, updating the character frequencies and
        comparing them to the target frequencies of s1.

        Args:
            s1 (str): The string whose permutation we are searching for.
            s2 (str): The string we are searching within.

        Returns:
            bool: True if s2 contains a permutation of s1, False otherwise.

        Time Complexity:
            O(L1 + L2): Where L1 is the length of `s1` and L2 is the length of `s2`.
            Building the initial dictionaries takes O(L1) time. Sliding the window
            takes O(L2 - L1) time. Comparing two dictionaries of size at most 26
            (lowercase English letters) takes O(1) time. Total time is strictly linear.

        Space Complexity:
            O(1): The dictionaries `s1_dict` and `freq` store character counts. Since
            the strings only consist of lowercase English letters, the dictionaries
            will hold a maximum of 26 key-value pairs. This means the space requirement
            is constant, regardless of how large the input strings are.
        """
        s1_len = len(s1)
        s2_len = len(s2)

        # If the target string is longer than the search string, a permutation is impossible
        if s2_len < s1_len:
            return False

        # s1_dict acts as our "recipe" to compare against
        s1_dict = defaultdict(int)

        # freq acts as our "current basket" of characters in the sliding window
        freq = defaultdict(int)

        # 1. Build a fixed window and populate both dictionaries for the first `s1_len` characters
        left = 0
        for right in range(s1_len):
            s1_dict[s1[right]] += 1
            freq[s2[right]] += 1

        # Check if the very first window is already a match
        if s1_dict == freq:
            return True

        # 2. Slide the window one character at a time through the rest of s2
        for right in range(s1_len, s2_len):
            # Add the new character entering the window from the right
            freq[s2[right]] += 1

            # Remove the oldest character leaving the window from the left
            freq[s2[left]] -= 1

            # If a character's count drops to 0, completely delete it from the dictionary.
            # This is critical! Python dictionary equality `==` checks keys as well.
            # `{'a': 1, 'b': 0}` does NOT equal `{'a': 1}`.
            if freq[s2[left]] == 0:
                del freq[s2[left]]

            # Move the left pointer forward to maintain the fixed window size
            left += 1  # noqa: SIM113

            # Compare our current window's frequency map to our target map
            if s1_dict == freq:
                return True

        return False


class Solution2:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Checks if a permutation of string s1 is a substring of string s2.

        This solution uses a Fixed-Size Sliding Window combined with Frequency Arrays.
        Since the problem guarantees only lowercase English letters, we can use
        arrays of size 26 to track character frequencies. This avoids the overhead
        of hash maps. We map characters 'a'-'z' to indices 0-25 using ASCII values.

        Args:
            s1 (str): The target string (we are looking for its permutation).
            s2 (str): The search string.

        Returns:
            bool: True if s2 contains a permutation of s1, False otherwise.

        Time Complexity:
            O(L1 + L2): Where L1 is the length of `s1` and L2 is the length of `s2`.
            We iterate through `s1` once to build the initial arrays. Then, we
            iterate through the remainder of `s2` once. Comparing two arrays of
            fixed size 26 takes O(1) time. Overall time is strictly linear.

        Space Complexity:
            O(1): We create exactly two arrays of size 26 (`s1_count` and `window_count`).
            Because this size is constant and independent of the input string lengths,
            the space complexity is strictly O(1).
        """
        s1_len = len(s1)
        s2_len = len(s2)

        # A permutation must be the exact same length as the target string.
        # If the search string is shorter, it's impossible.
        if s2_len < s1_len:
            return False

        # Use fixed-size arrays of 26 instead of dictionaries for faster access/comparison
        s1_count = [0] * 26
        window_count = [0] * 26

        # 1. Build the initial window
        # We process the first 's1_len' characters of both strings.
        # ord(char) - ord('a') maps 'a' to 0, 'b' to 1, ..., 'z' to 25.

        for right in range(s1_len):
            s1_count[ord(s1[right]) - ord("a")] += 1
            window_count[ord(s2[right]) - ord("a")] += 1

        # Check if the very first window happens to be a perfect match
        if s1_count == window_count:
            return True

        # 2. Slide the window one character at a time through the rest of s2
        for right in range(s1_len, s2_len):
            # Add the new character entering the window from the right
            window_count[ord(s2[right]) - ord("a")] += 1

            # Remove the oldest character leaving the window from the left.
            # Instead of a separate 'left' pointer, we mathematically calculate
            # the left index as (right - length of window).
            window_count[ord(s2[right - s1_len]) - ord("a")] -= 1

            # Compare our current 26-slot scorecard against the target scorecard
            if s1_count == window_count:
                return True

        return False
