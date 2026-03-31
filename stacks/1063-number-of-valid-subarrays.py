# Given an integer array nums, return the number of non-empty subarrays with the
# leftmost element of the subarray not larger than other elements in the subarray.

# A subarray is a contiguous part of an array.


# Example 1:

# Input: nums = [1,4,2,5,3]
# Output: 11
# Explanation: There are 11 valid subarrays: [1],[4],[2],[5],[3],[1,4],[2,5],
# [1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3].
# Example 2:

# Input: nums = [3,2,1]
# Output: 3
# Explanation: The 3 valid subarrays are: [3],[2],[1].
# Example 3:

# Input: nums = [2,2,2]
# Output: 6
# Explanation: There are 6 valid subarrays: [2],[2],[2],[2,2],[2,2],[2,2,2].


# Constraints:

# 1 <= nums.length <= 5 * 104
# 0 <= nums[i] <= 105


# Hint 1
# Given a data structure that answers queries of the type to find the minimum in
# a range of an array (Range minimum query (RMQ) sparse table) in O(1) time.
# How can you solve this problem?

# Hint 2
# For each starting index do a binary search with an RMQ to find the ending
# possible position.


class Solution:
    def validSubarrays(self, nums: list[int]) -> int:
        """
        Calculates the number of valid non-empty subarrays where the leftmost
        element is not larger than any other element in the subarray.

        Explainer:
        We use a "monotonic increasing stack" to store the indices of the elements.
        For each element at index `i`, we check if it is strictly smaller than
        the element at the top of the stack. If it is, the element at the top
        of the stack cannot extend its valid subarray any further.

        We pop the index `j` from the stack. The number of valid subarrays
        starting at `j` and ending just before `i` is exactly `i - j`.

        Any indices left in the stack after the loop never encountered a strictly
        smaller element. Their valid subarrays extend to the very end of the array,
        so we add `len(nums) - stack.pop()` to the total for each.

        Args:
            nums: A list of integers representing the input array.

        Returns:
            int: The total number of valid subarrays.

        Time Complexity:
            O(N): Where N is the number of elements in `nums`. Each index is
            pushed onto the stack exactly once and popped at most once.

        Space Complexity:
            O(N): In the worst-case scenario (e.g., a sorted increasing array
            like [1, 2, 3]), the stack will store all N indices.
        """
        ans = 0
        stack = []  # Tracks the indices of elements
        len_nums = len(nums)

        for i, elem in enumerate(nums):
            # If the current element is smaller than the element at the top of the stack,
            # it means the element at the top of the stack has found its rightmost boundary.
            while stack and nums[stack[-1]] > elem:
                j = stack.pop()
                # The number of valid subarrays starting at `j` is the distance between `i` and `j`
                ans += i - j

            # Push the current index onto the stack to process later
            stack.append(i)

        # Process any remaining indices in the stack.
        # These are elements that never found a smaller element to their right.
        while stack:
            # Their valid subarrays extend all the way to the end of the array.
            ans += len_nums - stack.pop()

        return ans


# ----
# Intuitive Explainer
# ----
# Instead of looking at the whole array, let's go number by number from left to
# right. At each step, we ask one question: **"How many valid starting points
# exist for a subarray that ends *right here*?"**

# **Step 1: We look at `1`**
# * What can start a valid subarray ending here? Just the `1`.
# * Valid subarray: `[1]`
# * **Our "Surviving Starters" list (the stack):** `[1]` *(Length = 1)*

# **Step 2: We look at `4`**
# * Can `1` still be a valid start? Yes, because $1 \le 4$. So `[1, 4]` is valid.
# * And `4` itself is a new valid start: `[4]`.
# * **Our "Surviving Starters" list:** `[1, 4]` *(Length = 2)*

# **Step 3: We look at `2` (Here is where the magic happens)**
# * We look at our previous starters: `1` and `4`.
# * Can `4` be the start of a valid subarray ending in `2`? That would be
# `[4, 2]`. **No!** Because $4 > 2$, the leftmost element is no longer the smallest.
# * In fact, `4` is now "dead" as a starting point forever. Any future subarray
# starting with `4` will contain this `2`, making it invalid. So, we kick `4`
# out of our list (this is the `pop()`!).
# * Can `1` still be a start? Yes, $1 \le 2$. `[1, 4, 2]` is valid.
# * And `2` itself is a new start: `[2]`.
# * **Our "Surviving Starters" list:** `[1, 2]` *(Length = 2)*

# **The Big Takeaway**
# The stack is literally just a list of **"surviving starting points"**.
# When a smaller number comes along, it acts like a wall. It "kills" any
# starting points bigger than it, because those bigger numbers can no longer
# be the smallest element in the subarray.

# Whatever is left in the stack + the new number itself = the exact number of
# valid subarrays ending at that specific moment.
