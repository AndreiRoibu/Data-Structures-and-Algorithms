# You are given an array of positive integers nums and want to erase a subarray
# containing unique elements. The score you get by erasing the subarray is equal
# to the sum of its elements.

# Return the maximum score you can get by erasing exactly one subarray.

# An array b is called to be a subarray of a if it forms a contiguous subsequence
#  of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).


# Example 1:

# Input: nums = [4,2,4,5,6]
# Output: 17
# Explanation: The optimal subarray here is [2,4,5,6].
# Example 2:

# Input: nums = [5,2,1,2,5,2,1,2,5]
# Output: 8
# Explanation: The optimal subarray here is [5,2,1] or [1,2,5].


# Constraints:

# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4

# Hint 1
# The main point here is for the subarray to contain unique elements for each
# index. Only the first subarrays starting from that index have unique elements.

# Hint 2
# This can be solved using the two pointers technique

from collections import defaultdict


class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        """Finds the maximum score of a subarray containing only unique elements.

        This solution uses the Sliding Window technique. We maintain a window
        [left, right] of unique elements. We expand the window by moving `right`
        and keep a running sum (`score`). If adding `nums[right]` creates a duplicate,
        we shrink the window from the `left` until the duplicate is removed,
        maintaining the "all unique" property.

        Args:
            nums (List[int]): An array of positive integers.

        Returns:
            int: The maximum sum (score) of any contiguous subarray with unique elements.

        Time Complexity:
            O(N): Where N is the length of `nums`.
            The `right` pointer iterates through the array exactly once. The `left`
            pointer also only moves forward. Each number is added to the window at most
            once and removed at most once. Dictionary lookups/updates are O(1) on average.
            Therefore, the total time is linear.

        Space Complexity:
            O(U): Where U is the number of unique elements in `nums` (in the worst case,
            U = N, making it O(N)).
            The `freq` dictionary stores the frequency of elements currently inside the
            sliding window.
        """
        left = 0

        # Dictionary to track the frequency of numbers currently in our window
        freq = defaultdict(int)

        # 'ans' stores the maximum score we have seen so far
        ans = 0

        # 'score' tracks the running sum of the numbers currently in our window
        score = 0

        # Iterate 'right' to expand the sliding window
        for right in range(len(nums)):
            elem = nums[right]

            # Add the new element to our frequency map and running score
            freq[elem] += 1
            score += elem

            # If the current element's frequency is > 1, our window has a duplicate!
            # We must shrink the window from the left until the duplicate is gone.
            while freq[nums[right]] > 1:
                # Deduct the left-most element from our frequency map and score
                freq[nums[left]] -= 1
                score -= nums[left]

                # Move the left pointer forward to officially shrink the window
                left += 1

            # Now that the while loop is done, we are guaranteed our window
            # only contains unique elements. Check if this is the highest score yet.
            ans = max(ans, score)

        return ans


class Solution2:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        """Finds the maximum score of a subarray containing only unique elements.

        This solution uses the Sliding Window technique combined with a Hash Set.
        We maintain a window [left, right] representing our current valid subarray.
        The `seen` set keeps track of the unique elements currently inside the window.
        If the element at the `right` pointer is already in the set, we shrink the
        window from the `left` until the duplicate is removed.

        Args:
            nums (List[int]): An array of positive integers.

        Returns:
            int: The maximum sum (score) of any contiguous subarray with strictly unique elements.

        Time Complexity:
            O(N): Where N is the length of `nums`.
            Both the `right` and `left` pointers only move forward through the array.
            Each element is added to the `seen` set exactly once and removed at most once.
            Since adding, removing, and checking membership (`in`) in a Python set
            are O(1) operations on average, the total time complexity is strictly linear.

        Space Complexity:
            O(U): Where U is the number of unique elements in `nums`.
            In the worst case (where all elements in the array are unique), the `seen`
            set will grow to hold all N elements, making the space complexity O(N).
        """
        # Pointer for the start of our sliding window
        left = 0

        # Hash set to track the unique elements currently inside our window
        seen = set()

        # 'ans' stores the maximum score we have found across all valid windows
        ans = 0

        # 'score' tracks the running sum of the numbers currently in our window
        score = 0

        # Expand the window by moving the 'right' pointer one step at a time
        for right in range(len(nums)):
            elem = nums[right]

            # If the new element is already in our window, the window is invalid.
            # We must shrink from the left until the duplicate is completely removed.
            while elem in seen:
                # Identify the element at the left edge of the window
                elem_left = nums[left]

                # Remove it from our set of active elements
                seen.remove(elem_left)

                # Deduct its value from our running score
                score -= elem_left

                # Move the left pointer forward to officially shrink the window
                left += 1

            # Now that the window is guaranteed to have only unique elements,
            # add the new element to our set and its value to our score.
            seen.add(elem)
            score += elem

            # Check if our current valid window has the highest score seen so far
            ans = max(ans, score)

        return ans
