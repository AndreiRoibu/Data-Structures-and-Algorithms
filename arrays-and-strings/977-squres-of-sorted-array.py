# Given an integer array nums sorted in non-decreasing order, return an array of
# the squares of each number sorted in non-decreasing order.

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        res = [0] * len_nums
        res_pos = len_nums - 1  # fill from the end
        left, right = 0, res_pos

        while left <= right:
            if abs(nums[left]) <= abs(nums[right]):
                res[res_pos] = nums[right] ** 2
                right -= 1
            else:
                res[res_pos] = nums[left] ** 2
                left += 1
            res_pos -= 1

        return res


# Explanation:
# - Use two pointers at the ends because the largest square comes from the
#   largest absolute value.
# - Place the larger square at the end of the result array and move inward.
# - Fill the result from right to left in a single pass.

# Time complexity: O(n) - we traverse the input array once
# Space complexity: O(n) - we create an output array of the same size as the input array
