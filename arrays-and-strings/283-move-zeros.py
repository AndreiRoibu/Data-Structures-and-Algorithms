# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.


# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]


# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = j = 0
        len_nums = len(nums)
        for i in range(len_nums):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        while j < len_nums:
            nums[j] = 0
            j += 1

        return nums


# Complexity Analysis:
# Time complexity: O(n), where n is the length of nums. We traverse the list twice.
# Space complexity: O(1), since we are modifying the list in place and not using
# any additional data structures that grow with input size.
