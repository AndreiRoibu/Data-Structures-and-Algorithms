# Two strings are considered close if you can attain one from the other using
# the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another
# existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close,
# and false otherwise.


# Example 1:

# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"
# Example 2:

# Input: word1 = "a", word2 = "aa"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in
# any number of operations.
# Example 3:

# Input: word1 = "cabbba", word2 = "abbccc"
# Output: true
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"

# Hint 1
# Operation 1 allows you to freely reorder the string.

# Hint 2
# Operation 2 allows you to freely reassign the letters' frequencies.


from collections import Counter, defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        Determines if two strings are "close" based on specific allowed operations.

        Explainer:
        Two strings are considered "close" if they satisfy two conditions:
        1. They contain the exact same set of unique characters (allows swapping characters).
        2. They have the same exact collection of character frequencies (allows transforming
           one character into another across the entire string).

        This solution first checks if the lengths match. Then, it iterates through both
        strings simultaneously to build frequency maps (`dct_word1`, `dct_word2`).
        Finally, it checks if both the unique characters (keys) and the sorted lists of
        frequencies (values) are identical.

        Args:
            word1 (str): The first string to compare.
            word2 (str): The second string to compare.

        Returns:
            bool: True if the strings are close, False otherwise.

        Complexity Analysis:
            Time Complexity: O(N) where N is the length of the strings.
                             Iterating through the strings of length N takes O(N) time.
                             Extracting keys and values, and sorting the values takes
                             O(K log K) time, where K is the number of unique characters.
                             Since there are at most 26 lowercase English letters,
                             K <= 26, making the sorting step effectively O(1). Thus,
                             the overall time complexity simplifies to O(N).
            Space Complexity: O(K) where K is the number of unique characters. Since K
                              is bounded by 26, the space required for the frequency
                              dictionaries simplifies to O(1) auxiliary space.
        """
        # Store lengths of both words in variables
        len_word1 = len(word1)
        len_word2 = len(word2)

        # If the lengths are different, they can't possibly be transformed into each other
        if len_word1 != len_word2:
            return False

        # Initialize dictionaries to keep track of character frequencies for both words
        dct_word1 = defaultdict(int)
        dct_word2 = defaultdict(int)

        # Iterate through the indices of both words simultaneously
        # (Since lengths are equal, we can safely use len_word1 for the range)
        for idx in range(len_word1):
            # Increment the count for the character at the current index in word1
            dct_word1[word1[idx]] += 1
            # Increment the count for the character at the current index in word2
            dct_word2[word2[idx]] += 1

        # For the words to be close, two conditions must be met:
        # 1. The sorted frequencies of characters must be exactly the same
        # 2. The set of unique characters present in both words must be exactly the same
        return (sorted(dct_word1.values()) == sorted(dct_word2.values())) and (dct_word1.keys() == dct_word2.keys())


# We can improve the execution speed and readability in Python:


class Solution2:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        dct_word1 = Counter(word1)
        dct_word2 = Counter(word2)

        return dct_word1.keys() == dct_word2.keys() and sorted(dct_word1.values()) == sorted(dct_word2.values())
