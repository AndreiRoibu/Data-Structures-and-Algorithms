# Given two strings s and t, return true if they are equal when both are typed
# into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.


# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# Example 3:

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".


# Constraints:

# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.


# Follow up: Can you solve it in O(n) time and O(1) space?


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_string(string):
            stack = []
            for char in string:
                if char != "#":
                    stack.append(char)
                elif stack:
                    stack.pop()

            return "".join(stack)

        return build_string(s) == build_string(t)


# Explanation:
# - Simulate typing with a stack, using "#" to pop when possible.
# - Build the final strings for s and t and compare them.

# Complexity Analysis
# Time Complexity: O(n + m), where n and m are the lengths of strings s and t
# respectively.
# Space Complexity: O(n + m) in the worst case, when there are no backspaces
#  in either string.
