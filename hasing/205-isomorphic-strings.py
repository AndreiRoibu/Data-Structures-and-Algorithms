# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to
# get t.

# All occurrences of a character must be replaced with another character while
#  preserving the order of characters. No two characters may map to the same
# character, but a character may map to itself.


# Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:

# Input: s = "f11", t = "b23"

# Output: false

# Explanation:

# The strings s and t can not be made identical as '1' needs to be mapped to
# both '2' and '3'.

# Example 3:

# Input: s = "paper", t = "title"

# Output: true


# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """Determines if two strings are isomorphic.

        Two strings are isomorphic if the characters in 's' can be replaced to get 't'.
        This requires a strict 1-to-1 (bijective) mapping between the characters of
        both strings. No two characters may map to the same character, and a character
        cannot map to two different characters.

        This solution uses two Hash Maps to maintain and verify this bi-directional
        relationship as we iterate through both strings simultaneously.

        Args:
            s (str): The first string.
            t (str): The second string (guaranteed to be the same length as s).

        Returns:
            bool: True if the strings are isomorphic, False otherwise.

        Time Complexity:
            O(N): Where N is the length of string `s` (or `t`).
            The `zip` function and the `for` loop iterate through the strings exactly
            once. Dictionary lookups (`in`), insertions, and `.get()` operations all
            take O(1) time on average. Therefore, the total time is linear.

        Space Complexity:
            O(1) strictly, or O(U) generally: Where U is the number of unique characters.
            The dictionaries `map_s_t` and `map_t_s` store the mappings. Because the
            problem uses standard ASCII characters, the maximum number of unique
            characters is bounded (usually 256). Thus, the space required will never
            exceed a constant maximum size, making it O(1). If the character set was
            infinite, it would be O(N) in the worst case.
        """
        # Dictionary to map a character from string 's' to a character in string 't'
        # map_s_t = defaultdict(str)
        map_s_t = {}

        # Dictionary to map a character from string 't' back to a character in string 's'
        # map_t_s = defaultdict(str)
        map_t_s = {}

        # NOTE: Using defaultdict(str) and actively checking if c1 not in
        # map_s_t is slightly dangerous. If we simply queried map_s_t[c1] to
        # check a value, it would automatically create a blank entry "" in the
        # dictionary! Because of how we wrote the code, it works with defaultdict,
        # but using standard dictionaries {} is safer and clearer for this
        # specific logic.

        # Iterate through both strings simultaneously, character by character
        for c1, c2 in zip(s, t, strict=False):
            # Scenario 1: We have never seen 'c1' AND we have never seen 'c2'.
            # We establish a brand new bi-directional mapping between them.
            if (c1 not in map_s_t) and (c2 not in map_t_s):
                map_s_t[c1] = c2
                map_t_s[c2] = c1

            # Scenario 2: We HAVE seen either 'c1' or 'c2' before.
            # We must verify that their established mappings match the current pairing.
            # If c1 maps to something other than c2, OR if c2 maps to something other than c1,
            # the 1-to-1 rule is broken!
            # Here, we use the `.get()` method to safely retrieve the mapped
            # values, which returns `None` if the key is not found, avoiding KeyErrors.
            elif map_s_t.get(c1) != c2 or map_t_s.get(c2) != c1:
                return False

        # If we successfully pair all characters without breaking the rules, they are isomorphic.
        return True
