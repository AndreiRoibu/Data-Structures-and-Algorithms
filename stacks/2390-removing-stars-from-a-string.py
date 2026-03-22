# You are given a string s, which contains stars *.

# In one operation, you can:

# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star
# itself.
# Return the string after all stars have been removed.

# Note:

# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.


# Example 1:

# Input: s = "leet**cod*e"
# Output: "lecoe"
# Explanation: Performing the removals from left to right:
# - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
# - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
# - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
# There are no more stars, so we return "lecoe".
# Example 2:

# Input: s = "erase*****"
# Output: ""
# Explanation: The entire string is removed, so we return an empty string.


# Constraints:

# 1 <= s.length <= 10^5
# s consists of lowercase English letters and stars *.
# The operation above can be performed on s.

# Hint 1
# What data structure could we use to efficiently perform these removals?

# Hint 2
# Use a stack to store the characters. Pop one character off the stack at each
# star. Otherwise, we push the character onto the stack.


class Solution:
    def removeStars(self, s: str) -> str:
        """
        Removes stars ('*') and the closest non-star character to their left.

        Explainer:
        This solution uses a stack data structure to process the string
        character by character. Because we need to remove the most recently
        seen valid character whenever we encounter a star, a stack follows
        the perfect Last-In-First-Out (LIFO) pattern. Regular characters are
        pushed onto the stack, and stars trigger a pop operation to remove
        the preceding character. Finally, the remaining characters are joined
        to form the answer.

        Args:
            s (str): The input string containing lowercase English letters and stars.

        Returns:
            str: The final string after all star-triggered removals are processed.

        Complexity Analysis:
            Time Complexity: O(N), where N is the length of the string `s`.
                             We iterate through the string exactly once, which takes
                             O(N) time. The `append()` and `pop()` operations on a
                             Python list (acting as a stack) take O(1) time on average.
                             Finally, `"".join(stack)` takes O(K) time where K is the
                             remaining characters. Overall time simplifies to O(N).
            Space Complexity: O(N), where N is the length of the string `s`.
                              In the worst-case scenario (e.g., a string with no stars
                              like "abcde"), the stack will store all N characters,
                              requiring linear auxiliary space.
        """
        # Initialize an empty list to act as our stack for tracking valid characters
        stack = []

        # Iterate through every character in the input string
        for char in s:
            # If the character is a regular letter, push it onto the stack
            if char != "*":
                stack.append(char)
            # If the character is a star, remove the most recently added letter
            else:
                stack.pop()

        # Combine the remaining characters in the stack into a final string and return
        return "".join(stack)
