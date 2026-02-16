# Given a string s, sort it in decreasing order based on the frequency of the
# characters. The frequency of a character is the number of times it appears in
# the string.

# Return the sorted string. If there are multiple answers, return any of them.


# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
# answer.
# Example 2:

# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and
# "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.


# Constraints:

# 1 <= s.length <= 5 * 105
# s consists of uppercase and lowercase English letters and digits.

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        """Sorts characters in a string based on their frequency in descending order.

        Uses `collections.Counter` to count character occurrences. The `most_common()`
        method returns a list of elements and their counts, sorted by count.
        We then construct the result string by repeating each character by its count.

        Args:
            s: The input string.

        Returns:
            A string with characters sorted by frequency.

        Time Complexity:
            O(N log K) or O(N) depending on implementation details, where N is the length
            of `s` and K is the number of unique characters.
            - Counting frequencies takes O(N).
            - Sorting the unique characters takes O(K log K).
            - Since the number of unique characters K is limited (e.g., typically 26-128 for ASCII),
              this can be considered O(N) in practice.
            - Building the result string takes O(N).

        Space Complexity:
            O(N) to store the result string and the frequency map (up to O(K) for the map).
        """
        ans = []
        counter = Counter(s)
        for key, value in counter.most_common():
            ans.append(key * value)
        return "".join(ans)


class Solution2:
    def frequencySort(self, s: str) -> str:
        """Sorts a string by character frequency in descending order using Bucket Sort.

        This implementation effectively achieves O(N) time complexity by avoiding
        comparison-based sorting. It is optimal when the number of unique characters (K)
        is large, or strictly linear time is required.

        Comparison with `Counter.most_common()` approach:
        - `Counter.most_common()` uses Timsort (O(K log K)) in C, which is often faster in
          Python practice due to low K (alphabet size) and C-level optimizations.
        - Bucket Sort is theoretically faster (O(N)) as N grows or if K is proportional to N,
          but suffers from Python's interpreter loop overhead.

        This implementation uses the "Bucket Sort" pattern:
        1. Frequencies determine the index in a bucket array.
        2. Indices are iterated in reverse to ensure descending order.

        Args:
            s: The input string.

        Returns:
            The string sorted by character frequency.

        Time Complexity:
            O(N), where N is the length of `s`.
            - Counting frequencies: O(N).
            - Populating buckets: O(K), where K is unique characters (K <= N).
            - Building result: O(N) (iterating through all characters in buckets).
            Total is linear.

        Space Complexity:
            O(N).
            - We store frequency counts: O(K).
            - The `buckets` array stores all characters distributed across lists: O(N).
            - The result string: O(N).
        """
        if not s:
            return s

        # 1. Count frequencies of each character
        counts = Counter(s)

        # 2. Determine maximum frequency to size the buckets array efficiently
        # This prevents creating unnecessary empty buckets if max_freq << len(s)
        max_freq = max(counts.values())

        # 3. Initialize buckets
        # Index i stores a list of characters that appear exactly i times.
        # Size is max_freq + 1 to accommodate 1-based frequency indexing.
        buckets = [[] for _ in range(max_freq + 1)]

        # 4. Populate buckets
        for char, freq in counts.items():
            buckets[freq].append(char)

        # 5. Build the result string
        # Iterate backwards from highest frequency to 1
        ans = []
        for freq in range(max_freq, 0, -1):
            for char in buckets[freq]:
                # Append the character `freq` times
                ans.append(char * freq)

        return "".join(ans)
