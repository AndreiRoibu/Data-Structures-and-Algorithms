# You are given a string s consisting of lowercase English letters. A duplicate
# removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made.
# It can be proven that the answer is unique.


# Example 1:

# Input: s = "abbaca"
# Output: "ca"
# Explanation:
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
# Example 2:

# Input: s = "azxxzy"
# Output: "ay"


# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)


# Explanation:
# - Use a stack to track the current characters.
# - If the next character matches the stack top, remove the pair.
# - The stack contents form the final string.

# Complexity Analysis:
# Time Complexity: O(N), where N is the length of the string s. We traverse
# the string once.
# Space Complexity: O(N) in the worst case, where all characters in s are
# unique, and we store all of them in the stack.
