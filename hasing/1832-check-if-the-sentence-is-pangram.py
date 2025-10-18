# A pangram is a sentence where every letter of the English alphabet appears at
# least once.

# Given a string sentence containing only lowercase English letters, return true
# if sentence is a pangram, or false otherwise.


# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:

# Input: sentence = "leetcode"
# Output: false


# Constraints:

# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()
        for char in sentence:
            seen.add(char)
        return len(seen) == 26


# Complexity Analysis:
# Time complexity: O(n), where n is the length of the sentence. We traverse the
# entire sentence once to add characters to the set.
# Space complexity: O(1), since the size of the set is bounded by the number of
# letters in the English alphabet, which is 26.
