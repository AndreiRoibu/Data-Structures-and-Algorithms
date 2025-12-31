# Given an array of integers nums which is sorted in ascending order, and an
# integer target, write a function to search target in nums. If target exists,
# then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1


# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            num = nums[mid]

            if num == target:
                return mid

            if num > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1


# Explanation:
# - Maintain left and right bounds of the sorted array.
# - Check the middle element and discard half the search space each step.
# - Return the index when found; otherwise return -1.

# Complexity Analysis:
# Time Complexity: O(log N), where N is the length of nums.
# We halve the search space at each step of the binary search, leading to a
# logarithmic time complexity.
# Space Complexity: O(1). We use only a constant amount of extra space.
