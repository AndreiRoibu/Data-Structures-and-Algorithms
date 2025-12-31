# Given an array of strings strs, group the anagrams together. You can
# return the answer in any order.


# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged
# to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be
# rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]


# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English lett

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        seen = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            seen[key].append(s)

        return list(seen.values())


# Explanation:
# - Use the sorted characters of each string as a canonical anagram key.
# - Group strings by this key in a dictionary.
# - Return the grouped values.

# Complexity Analysis:
# Time complexity: O(NKlogK), where N is the length of strs, and K is
# the maximum length of a string in strs.
# Space complexity: O(NK), the total information content stored in
# ans.
