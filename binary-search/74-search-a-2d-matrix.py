# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous
# row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.


# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        while left <= right:
            mid = (left + right) // 2
            row_idx = mid // cols
            col_idx = mid % cols
            num = matrix[row_idx][col_idx]

            if num == target:
                return True
            if num < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


# Explanation:
# - Treat the matrix as a sorted 1D array of length rows * cols.
# - Use binary search and map mid to (row, col) via division and modulo.
# - Compare the mapped value to target and shrink the search space.

# Complexity Analysis:
# Time Complexity: O(log(m * n)), where m is the number of rows and n is the
# number of columns in the matrix. We are performing a binary search on the
# entire matrix, which has m * n elements.
# Space Complexity: O(1), as we are using only a constant amount of extra space.
