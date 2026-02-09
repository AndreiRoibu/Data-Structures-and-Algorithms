# You are given two strings s and t of the same length and an integer maxCost.

# You want to change s to t. Changing the ith character of s to ith character
# of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII
# values of the characters).

# Return the maximum length of a substring of s that can be changed to be the
# same as the corresponding substring of t with a cost less than or equal to
# maxCost. If there is no substring from s that can be changed to its
# corresponding substring from t, return 0.


# Example 1:

# Input: s = "abcd", t = "bcdf", maxCost = 3
# Output: 3
# Explanation: "abc" of s can change to "bcd".
# That costs 3, so the maximum length is 3.
# Example 2:

# Input: s = "abcd", t = "cdef", maxCost = 3
# Output: 1
# Explanation: Each character in s costs 2 to change to character in t,  so the
# maximum length is 1.
# Example 3:

# Input: s = "abcd", t = "acde", maxCost = 0
# Output: 1
# Explanation: You cannot make any change, so the maximum length is 1.


# Constraints:

# 1 <= s.length <= 105
# t.length == s.length
# 0 <= maxCost <= 106
# s and t consist of only lowercase English letters.

# Hint 1
# Calculate the differences between s[i] and t[i].
# Hint 2
# Use a sliding window to track the longest valid substring.


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = cost = ans = 0
        for right in range(len(s)):
            cost += abs(ord(s[right]) - ord(t[right]))
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans, right - left + 1)
        return ans


# Explanation:

# **Algorithm: Sliding Window**

# - **Goal**: Find longest substring where conversion cost ≤ maxCost
# - **Window tracking**: `[left, right]` represents current valid substring
# - **Cost calculation**: `abs(ord(s[i]) - ord(t[i]))` for each position
# - **Expand window**: Move `right` pointer to include new characters
# - **Shrink window**: When cost exceeds maxCost, move `left` pointer to reduce cost
# - **Track maximum**: Update answer with window size `right - left + 1` at each valid state

# **Key Insights**
# - Each character enters and exits window at most once → O(n) time
# - Window always maintains valid state (cost ≤ maxCost)
# - Maximum window size during traversal = answer

# **Edge Cases Handled**
# - Empty strings (returns 0)
# - maxCost = 0 (only matching characters count)
# - maxCost ≥ total cost (returns full string length)

# **Why it works**: Greedy expansion with minimal contraction ensures we explore all possible valid substrings efficiently.

# Complexity Analysis:
# - Time Complexity O(n): The outer for loop iterates through each character once
# (n iterations)
# - Space Complexity O(1): Constant space is needed.
