# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.


# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"

# Output: true

# Explanation:

# The bijection can be established as:

# 'a' maps to "dog".
# 'b' maps to "cat".
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"

# Output: false

# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"

# Output: false


# Constraints:

# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """Determines if a string 's' follows the exact same pattern as 'pattern'.

        This solution uses a Two-Way Hash Map (Bijection) to enforce a strict
        1-to-1 relationship between characters in the pattern and words in the string.
        It maintains two dictionaries: one mapping pattern characters to words,
        and another mapping words back to pattern characters. This prevents scenarios
        where multiple pattern characters map to the same word.

        Args:
            pattern (str): A string consisting of single characters representing a pattern.
            s (str): A string consisting of space-separated words.

        Returns:
            bool: True if 's' perfectly follows 'pattern', False otherwise.

        Time Complexity:
            O(N + M): Where N is the number of characters in `pattern` and M is the total
            number of characters in `s`. Splitting `s` into words takes O(M) time.
            Zipping and iterating through the lists takes O(N) time. Dictionary
            lookups and insertions take O(1) time on average.

        Space Complexity:
            O(N + W): Where N is the number of unique characters in `pattern` and W is
            the number of unique words in `s`. We create two hash maps that store these
            unique elements. Additionally, `s.split()` creates a list of words, which
            takes space proportional to the length of string `s`.
        """
        # Dictionary to map a pattern character to an English word
        pattern_to_s = {}

        # Dictionary to map an English word back to a pattern character
        s_to_pattern = {}

        # Split the single string 's' into a list of individual words based on spaces
        s_words = s.split()

        # A basic check: if the number of pattern letters doesn't match
        # the number of words, a 1-to-1 mapping is mathematically impossible.
        if len(pattern) != len(s_words):
            return False

        # zip() pairs up the pattern character and the corresponding word at the same index
        for c1, c2 in zip(pattern, s_words, strict=False):
            # Scenario 1: Both the character and the word are completely new.
            # We add them to both of our translation dictionaries.
            if (c1 not in pattern_to_s) and (c2 not in s_to_pattern):
                pattern_to_s[c1] = c2
                s_to_pattern[c2] = c1

            # Scenario 2: We have seen either the character or the word before.
            # We must verify that their established translations match the current pairing.
            # We use .get() because one of them might exist while the other doesn't,
            # and .get() safely returns None instead of throwing a KeyError.
            elif pattern_to_s.get(c1) != c2 or s_to_pattern.get(c2) != c1:
                return False

        # If we successfully iterate through the entire string without finding
        # any translation contradictions, the pattern is valid.
        return True
