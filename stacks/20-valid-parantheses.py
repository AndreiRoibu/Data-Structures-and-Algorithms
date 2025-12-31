# Given a string s containing just the characters '(', ')', '{', '}',
# '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if not stack:
                    return False
                last_open = stack.pop()
                if pairs[last_open] != char:
                    return False

        return not stack


# Explanation:
# - Push opening brackets onto a stack.
# - On a closing bracket, pop and verify the types match.
# - The string is valid only if the stack is empty at the end.

# Complexity Analysis:
# Time Complexity: O(N), where N is the length of the input string s. We
# traverse the string once.
# Space Complexity: O(N) in the worst case, where all characters in the
# string are opening brackets. In this case, we would push all opening
# brackets onto the stack.
