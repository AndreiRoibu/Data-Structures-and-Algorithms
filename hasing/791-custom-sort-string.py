# You are given two strings order and s. All the characters of order are unique
# and were sorted in some custom order previously.

# Permute the characters of s so that they match the order that order was sorted.
# More specifically, if a character x occurs before a character y in order,
# then x should occur before y in the permuted string.

# Return any permutation of s that satisfies this property.


# Example 1:

# Input: order = "cba", s = "abcd"

# Output: "cbad"

# Explanation:  "a", "b", "c" appear in order, so the order of "a", "b", "c"
# should be "c", "b", and "a".

# Since "d" does not appear in order, it can be at any position in the returned
# string. "dcba", "cdba", "cbda" are also valid outputs.

# Example 2:

# Input: order = "bcafg", s = "abcd"

# Output: "bcad"

# Explanation: The characters "b", "c", and "a" from order dictate the order for
# the characters in s. The character "d" in s does not appear in order, so its
# position is flexible.

# Following the order of appearance in order, "b", "c", and "a" from s should be
# arranged as "b", "c", "a". "d" can be placed at any position since it's not
# in order. The output "bcad" correctly follows this rule. Other arrangements
# like "dbca" or "bcda" would also be valid, as long as "b", "c", "a" maintain
# their order.


# Constraints:

# 1 <= order.length <= 26
# 1 <= s.length <= 200
# order and s consist of lowercase English letters.
# All the characters of order are unique.


from collections import defaultdict


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        Sorts the characters of string `s` based on a custom `order`.

        Explainer:
        This solution counts the frequency of each character in `s`. It then iterates
        through the custom `order` string, appending each character to the result array
        as many times as it appeared in `s`, and then removes it from the frequency map.
        Finally, it appends any remaining characters from `s` that were not present in
        `order` to the result array before joining it into the final string.

        Args:
            order (str): A string of unique characters representing the desired sorting order.
            s (str): The string to be sorted.

        Returns:
            str: The rearranged string matching the custom order.

        Complexity Analysis:
            Time Complexity: O(N + M), where N is the length of `s` and M is the length
                             of `order`. Constructing the counter takes O(N). Iterating
                             through `order` takes O(M), and appending characters takes
                             O(N) operations in total across all loops. Since M <= 26
                             (lowercase English letters), this simplifies to O(N).
            Space Complexity: O(N) for the `ans` array used to build the final string.
                              The `s_counter` dictionary takes O(1) space because there
                              are at most 26 unique lowercase English letters.
        """
        # Dictionary to keep track of the frequencies of each character in 's'
        s_counter = defaultdict(int)

        # Populate the frequency map
        for char in s:
            s_counter[char] += 1

        ans = []

        # Iterate through the custom order to ensure characters are added in the right sequence
        for char in order:
            if char in s_counter:
                # Append the character as many times as it appears in 's'
                ans.append(char * s_counter[char])

                # Delete the character from the map to track which characters are left over
                del s_counter[char]

        # If there are any characters left in 's' that weren't in 'order', append them
        if s_counter:
            for char, count in s_counter.items():
                ans.append(char * count)

        # Join the list of characters into a single string and return
        return "".join(ans)
