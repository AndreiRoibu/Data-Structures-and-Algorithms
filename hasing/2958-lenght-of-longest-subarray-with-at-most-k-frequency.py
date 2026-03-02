# You are given an integer array nums and an integer k.

# The frequency of an element x is the number of times it occurs in an array.

# An array is called good if the frequency of each element in this array is less
# than or equal to k.

# Return the length of the longest good subarray of nums.

# A subarray is a contiguous non-empty sequence of elements within an array.


# Example 1:

# Input: nums = [1,2,3,1,2,3,1,2], k = 2
# Output: 6
# Explanation: The longest possible good subarray is [1,2,3,1,2,3] since the
# values 1, 2, and 3 occur at most twice in this subarray. Note that the
# subarrays [2,3,1,2,3,1] and [3,1,2,3,1,2] are also good.
# It can be shown that there are no good subarrays with length more than 6.
# Example 2:

# Input: nums = [1,2,1,2,1,2,1,2], k = 1
# Output: 2
# Explanation: The longest possible good subarray is [1,2] since the values 1
# and 2 occur at most once in this subarray. Note that the subarray [2,1] is
#   also good.
# It can be shown that there are no good subarrays with length more than 2.
# Example 3:

# Input: nums = [5,5,5,5,5,5,5], k = 4
# Output: 4
# Explanation: The longest possible good subarray is [5,5,5,5] since the value
# 5 occurs 4 times in this subarray.
# It can be shown that there are no good subarrays with length more than 4.


# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= nums.length

# Hint 1
# For each index i, find the rightmost index j >= i such that the frequency of
# each element in the subarray [i, j] is at most k.

# Hint 2
# We can use 2 pointers / sliding window to achieve it.

from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        """Finds the length of the longest subarray where no element appears more than k times.

        This solution uses the Sliding Window technique. It maintains a dynamic window
        defined by the indices [left, right] and uses a hash map (`frequency`) to track
        the occurrences of elements currently inside the window.

        As the `right` pointer expands the window, if the newly added element's frequency
        exceeds `k`, the `left` pointer shrinks the window from the left until the
        violating element's frequency drops back to `k`. The maximum valid window size
        is recorded at each step.

        Args:
            nums (List[int]): An array of integers.
            k (int): The maximum allowed frequency for any element in the subarray.

        Returns:
            int: The length of the longest valid subarray.

        Time Complexity:
            O(N): Where N is the length of `nums`.
            The `right` pointer iterates through the array exactly once. The `left`
            pointer also strictly moves forward from 0 to N. This means each element
            is processed (added to and removed from the hash map) at most twice.
            Since hash map operations (insert/lookup) are O(1) on average, the overall
            time is bounded by O(2N), which simplifies to O(N).

        Space Complexity:
            O(N): In the worst case (where all elements in the array are unique),
            the `frequency` dictionary will need to store an entry for every single
            element in the input array, scaling linearly with the input size.
        """
        # Initialize the left pointer of our sliding window
        left = 0

        # Dictionary to keep track of the count of elements currently in the window
        frequency = defaultdict(int)

        # Variable to store the length of the longest valid subarray found so far
        ans = 0

        # Iterate the right pointer to expand the window element by element
        for right in range(len(nums)):
            # Add the current element to our window's frequency map
            frequency[nums[right]] += 1

            # If the current element's frequency exceeds the allowed limit 'k',
            # our window is invalid. We must shrink it from the left.
            while frequency[nums[right]] > k:
                # Decrease the frequency of the element at the 'left' pointer
                # as it falls out of the window
                frequency[nums[left]] -= 1

                # Move the left pointer forward to shrink the window
                left += 1

            # At this point, the while loop has guaranteed our window is valid.
            # Calculate the current window's size (right - left + 1) and update the max.
            ans = max(ans, right - left + 1)

        return ans
