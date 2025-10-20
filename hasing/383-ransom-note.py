# Given two strings ransomNote and magazine, return true if ransomNote can be
# constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.


# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true


# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # ---
        # Solution 1.1 - dictionary
        # ---
        letters = {}
        for character in magazine:
            if character in letters:
                letters[character] += 1
            else:
                letters[character] = 1

        for character in ransomNote:
            if character not in letters:
                return False
            else:
                letters[character] -= 1
                if letters[character] < 0:
                    return False

        return True

        # ---
        # Solution 2 - Counter
        # ---
        # Counter(ransomNote) counts each needed letter.
        # Counter(ransomNote) - Counter(magazine) subtracts available letters;
        # The "not" checks if any letter is missing (i.e., has a negative count).
        # any letter with a negative or zero count is removed, so if the result is empty,
        # every need was met.

        # return not (Counter(ransomNote) - Counter(magazine))


# Complexity Analysis:
# Time Complexity: O(N + M), where N is the length of ransomNote and M is the length of magazine.
# We traverse both strings once to build the frequency dictionary and check
# the availability of letters.
# Space Complexity: O(1), since the dictionary will hold at most 26 key-value pairs
# for each letter in the English alphabet.
