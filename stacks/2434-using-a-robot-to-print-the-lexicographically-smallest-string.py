# You are given a string s and a robot that currently holds an empty string t.
# Apply one of the following operations until s and t are both empty:

# Remove the first character of a string s and give it to the robot. The robot
# will append this character to the string t.
# Remove the last character of a string t and give it to the robot. The robot
# will write this character on paper.
# Return the lexicographically smallest string that can be written on the paper.


# Example 1:

# Input: s = "zza"
# Output: "azz"
# Explanation: Let p denote the written string.
# Initially p="", s="zza", t="".
# Perform first operation three times p="", s="", t="zza".
# Perform second operation three times p="azz", s="", t="".
# Example 2:

# Input: s = "bac"
# Output: "abc"
# Explanation: Let p denote the written string.
# Perform first operation twice p="", s="c", t="ba".
# Perform second operation twice p="ab", s="c", t="".
# Perform first operation p="ab", s="", t="c".
# Perform second operation p="abc", s="", t="".
# Example 3:

# Input: s = "bdda"
# Output: "addb"
# Explanation: Let p denote the written string.
# Initially p="", s="bdda", t="".
# Perform first operation four times p="", s="", t="bdda".
# Perform second operation four times p="addb", s="", t="".


# Constraints:

# 1 <= s.length <= 105
# s consists of only English lowercase letters.


# Hint 1
# If there are some character “a”' s in the string, they can be written on
# paper before anything else.

# Hint 2
# Every character in the string before the last “a” should be written in
# reversed order.

# Hint 3
# After the robot writes every “a” on paper, the same holds for other characters
# “b”, ”c”, …etc.


from collections import Counter


class Solution:
    def robotWithString(self, s: str) -> str:
        """
        Simulates a robot to find the lexicographically smallest string that can be
        printed using a stack.

        Explainer:
        To get the lexicographically smallest string, we want to print the smallest
        possible characters as early as possible. In other words, among all
        possible output strings the robot could write, choose the one that would
        come first in dictionary order.

        We use `t_stack` to represent the
        robot's string 't', and a frequency map `counter` to keep track of characters
        we haven't processed yet.

        As we iterate through the string `s`, we push the current character onto `t_stack`
        and decrease its remaining count. The key insight is: we should only pop from
        `t_stack` (i.e., print to the paper) if the character at the top of the stack
        is smaller than or equal to the smallest character (`minChar`) remaining in `s`.
        If a smaller character exists later in the string, we must wait and push characters
        onto the stack until we reach it.

        Args:
            s (str): The initial string given to the robot.

        Returns:
            str: The lexicographically smallest string that can be written on the paper.

        Complexity Analysis:
            Time Complexity: O(N), where N is the length of the string `s`. Counting
                             the frequencies takes O(N). We iterate through `s` exactly
                             once. Each character is pushed to and popped from `t_stack`
                             at most once, taking O(N) time. The inner `while minChar != 'z'`
                             loop only increments at most 25 times across the entire function
                             run (since the alphabet has 26 letters). Thus, the total time
                             is strictly O(N).
            Space Complexity: O(N), where N is the length of `s`. The `t_stack` and `ans`
                              arrays can each store up to N characters. The `Counter` takes
                              O(1) auxiliary space since it stores at most 26 keys (for
                              lowercase English letters). Overall space is O(N).
        """
        # t_stack acts as the intermediate string 't'
        t_stack = []
        # ans acts as the "paper" where we print our final string
        ans = []

        # Keep track of the frequencies of the remaining characters in 's'
        counter = Counter(s)

        # Keep track of the globally smallest character remaining in the unprocessed part of 's'
        minChar = "a"

        # Iterate through the given string
        for char in s:
            # The robot's first operation: add character to string 't' (our stack)
            t_stack.append(char)
            # We just processed this character, so it's no longer "remaining" in 's'
            counter[char] -= 1

            # Update minChar: If we have exhausted all occurrences of the current minChar
            # in the remaining string, we need to find the next smallest available character.
            while minChar != "z" and counter[minChar] == 0:
                # Move minChar to the next letter in the alphabet
                minChar = chr(ord(minChar) + 1)

            # The robot's second operation: write from string 't' to the paper.
            # We greedily pop and append to our answer AS LONG AS the top of the stack
            # is smaller than or equal to the smallest character left in the remaining string.
            # If the top of the stack is > minChar, we must wait because a better (smaller)
            # character is coming up!
            while t_stack and t_stack[-1] <= minChar:
                ans.append(t_stack.pop())

        # Join the list of printed characters into a single string
        return "".join(ans)
