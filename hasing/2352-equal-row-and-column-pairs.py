# Given a 0-indexed n x n integer matrix grid, return the number of pairs
# (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements
# in the same order (i.e., an equal array).


# Example 1:


# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]
# Example 2:


# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]


# Constraints:

# n == grid.length == grid[i].length
# 1 <= n <= 200
# 1 <= grid[i][j] <= 105


from collections import defaultdict

import numpy as np


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        dct_rows = defaultdict(int)
        dct_cols = defaultdict(int)
        grid = np.array(grid)

        for row in grid:
            dct_rows[tuple(row)] += 1

        for col in grid.T:
            dct_cols[tuple(col)] += 1

        answer = 0
        for elem in dct_rows:
            answer += dct_rows[elem] * dct_cols[elem]

        return answer


# Complexity Analysis:
# Time Complexity: O(N^2), where N is the number of rows (or columns) in the grid.
# This is because we iterate through each row and each column of the grid
# to populate the dictionaries, which takes O(N^2) time.
# Space Complexity: O(N^2) in the worst case, where all rows and columns are unique.
# This is because we store each unique row and column in the dictionaries.


class Solution2:
    def equalPairs(self, grid: list[list[int]]) -> int:
        dct_rows = defaultdict(int)
        dct_cols = defaultdict(int)
        n = len(grid)

        for idx in range(n):
            dct_rows[tuple(grid[idx])] += 1
            current_col = []
            for row in range(n):
                current_col.append(grid[row][idx])
            dct_cols[tuple(current_col)] += 1

        answer = 0
        for elem in dct_rows:
            answer += dct_rows[elem] * dct_cols[elem]

        return answer
