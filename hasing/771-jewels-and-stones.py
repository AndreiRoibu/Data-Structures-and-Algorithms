# You're given strings jewels representing the types of stones that are jewels,
# and stones representing the stones you have. Each character in stones is a
# type of stone you have. You want to know how many of the stones you have are
# also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".


# Example 1:

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:

# Input: jewels = "z", stones = "ZZ"
# Output: 0


# Constraints:

# 1 <= jewels.length, stones.length <= 50
# jewels and stones consist of only English letters.
# All the characters of jewels are unique.

from collections import defaultdict


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        seen = defaultdict(int)
        for stone in stones:
            if stone in jewels:
                seen[stone] += 1
        return sum(seen.values())


# Explanation:
# - Scan each stone and check whether it is a jewel type.
# - Count matching stones in a dictionary and sum the counts at the end.

# Complexity Analysis:
# Time Complexity: O(S * J), where S is the length of stones and J is the
# length of jewels, since membership checks scan the jewels string. With J
# bounded by 52, this is effectively O(S).
# Space Complexity: O(J), where J is the length of the jewels string. In the
# worst case, we may store all jewel types in the seen dictionary. Can be O(1)
# since the number of possible jewel types is limited to 52 (26 lowercase and
# 26 uppercase English letters).
