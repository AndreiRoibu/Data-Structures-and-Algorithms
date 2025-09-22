# Write a function that reverses a string. The input string is given as an array
# of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


# Constraints:

# 1 <= s.length <= 105
# s[i] is a printable ascii character.


class Solution:
    def reverseString(self, s: List[str]) -> None:  # noqa: F821
        """
        Do not return anything, modify s in-place instead.
        """
        lp = 0
        rp = len(s) - 1
        while lp <= rp:
            saved_letter = s[lp]
            s[lp] = s[rp]
            s[rp] = saved_letter
            lp += 1
            rp -= 1


# Complexity Analysis:
# Time complexity : O(n) since we traverse the input string once.
# Space complexity : O(1) since we use only constant space.
