# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.


# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.


# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
# 1 <= k <= s.length


# Hint 1
# Keep a window of size k and maintain the number of vowels in it.


# Hint 2
# Keep moving the window and update the number of vowels while moving. Answer is
# max number of vowels of any window.


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}

        count = 0
        for i in range(k):
            count += int(s[i] in vowels)
        answer = count

        for i in range(k, len(s)):
            count += int(s[i] in vowels)
            count -= int(s[i - k] in vowels)
            answer = max(answer, count)

        return answer


# Explanation:
# - We define a set of vowels for quick lookup.
# - We initialize a count of vowels in the first window of size k.
# - We then slide the window across the string, updating the count by adding the
# new character and removing the character that is no longer in the window.
# - We keep track of the maximum count of vowels found in any window and return it.

# Complexity Analysis:
# - Time Complexity: O(n), where n is the length of the string s. We traverse the string once.
# - Space Complexity: O(1), since the space used for the vowels set is constant.
