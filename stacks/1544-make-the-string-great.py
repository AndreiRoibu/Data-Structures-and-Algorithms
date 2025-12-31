# Given a string s of lower and upper case English letters.

# A good string is a string which doesn't have two adjacent characters s[i]
# and s[i + 1] where:

# 0 <= i <= s.length - 2
# s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case
# or vice-versa.
# To make the string good, you can choose two adjacent characters that make the
#  string bad and remove them. You can keep doing this until the string becomes
# good.

# Return the string after making it good. The answer is guaranteed to be unique
# under the given constraints.

# Notice that an empty string is also good.


# Example 1:

# Input: s = "leEeetcode"
# Output: "leetcode"
# Explanation: In the first step, either you choose i = 1 or i = 2, both will
# result "leEeetcode" to be reduced to "leetcode".
# Example 2:


# Input: s = "abBAcC"
# Output: ""
# Explanation: We have many possible scenarios, and all lead to the same answer.
#  For example:
# "abBAcC" --> "aAcC" --> "cC" --> ""
# "abBAcC" --> "abBA" --> "aA" --> ""
# Example 3:

# Input: s = "s"
# Output: "s"


# Constraints:

# 1 <= s.length <= 100
# s contains only lower and upper case English letters.


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)


# Explanation:
# - Use a stack to keep characters that are part of the current good string.
# - Adjacent letters that differ only by case have an ASCII gap of 32, so pop them.
# - The remaining stack forms the final good string.

# Complexity Analysis:
# Time complexity: O(n), where n is the length of the string s. We traverse the
# string once, and each character is pushed and popped from the stack at most
# once.
# Space complexity: O(n) in the worst case, where all characters in the string s
# are distinct and none of them can be removed. In this case, the stack will
# contain all n characters.
