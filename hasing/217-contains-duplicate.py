# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.


# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true


# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)


# - **Summary explainer (for future reference)**
#   - Convert `nums` to a `set` (automatically removes any duplicates).
#   - Compare lengths: if `set(nums)` is smaller than `nums`, duplicates existed.
#   - Returns `True` if duplicate found, `False` otherwise.

# - **Time Complexity: O(n)**
#   - Creating a set requires iterating through all `n` elements.
#   - Each insertion into the hash set is O(1) average case.
#   - Computing `len()` is O(1) for both list and set.

# - **Space Complexity: O(n)**
#   - The set stores up to `n` unique elements in the worst case (when all elements are distinct).
#   - This is the trade-off for the O(n) time solution—using extra space to detect duplicates efficiently.
#   - Worst case: if all elements are unique, the set contains all `n` elements.
