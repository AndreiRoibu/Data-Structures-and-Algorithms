# Given a string s, reverse the string according to the following rules:

# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.


# Example 1:

# Input: s = "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:

# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"


# Constraints:

# 1 <= s.length <= 100
# s consists of characters with ASCII values in the range [33, 122].
# s does not contain '\"' or '\\'.


# Hint 1
# This problem is exactly like reversing a normal string except that there are
# certain characters that we have to simply skip. That should be easy enough to
# do if you know how to reverse a string using the two-pointer approach.


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not chars[right].isalpha():
                right -= 1
            while left < right and not chars[left].isalpha():
                left += 1
            chars[left], chars[right] = chars[right], chars[left]
            right -= 1
            left += 1
        return "".join(chars)


# Explanation:
# - Convert the string to a list so we can swap characters in place.
# - Use two pointers to find letters from both ends, swapping them when found.
# - Join the list back into a string after all swaps.

# Complexity Analysis:
# Time complexity: O(n), where n is the length of s. Each character is processed
# at most once.
# Space complexity: O(n), since we convert the string to a list of characters
# which takes additional space proportional to the size of the input string.

# ---- Other Solutions ----


class Solution2:
    def reverseOnlyLetters(self, S):
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)


# Explanation:
# - Extract all letters from the string and store them in a list.
# - Iterate through the original string, replacing letters with the last letter
# from the list, effectively reversing their order.
# - Non-letter characters are added to the result as they are.

# Complexity Analysis:
# Time complexity: O(n), where n is the length of S. We traverse the string
# multiple times but each operation is linear.
# Space complexity: O(n), for storing the letters in a separate list.


class Solution3:
    def reverseOnlyLetters(self, S):
        ans = []
        j = len(ans) - 1
        for _, x in enumerate(S):
            if x.isalpha():
                while not S[j].isalpha():
                    j -= 1
                ans.append(S[j])
                j -= 1
            else:
                ans.append(x)

        return "".join(ans)

    # Explanation:
    # - Use a pointer j starting from the end of the string to find letters.
    # - For each character in the string, if it's a letter, append the letter
    # found by j; otherwise, append the character itself.
    # - This effectively reverses the letters while keeping non-letters in place.

    # Complexity Analysis:
    # Time complexity: O(n), where n is the length of S. Each character is
    # processed once.
    # Space complexity: O(n), for storing the result in a list before joining
    # into a string.
