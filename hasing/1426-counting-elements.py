# Given an integer array arr, count how many elements x there are, such
# that x + 1 is also in arr. If there are duplicates in arr, count them
# separately.


# Example 1:

# Input: arr = [1,2,3]
# Output: 2
# Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
# Example 2:

# Input: arr = [1,1,3,3,5,5,7,7]
# Output: 0
# Explanation: No numbers are counted, cause there is no 2, 4, 6, or 8 in arr.


# Constraints:

# 1 <= arr.length <= 1000
# 0 <= arr[i] <= 1000


class Solution:
    def countElements(self, arr: list[int]) -> int:
        answer = 0
        elements = set(arr)
        for x in arr:
            if x + 1 in elements:
                answer += 1

        return answer


# Explanation:
# - Store all values in a set for O(1) membership checks.
# - Count each element whose value + 1 also exists in the set.

# Complexity Analysis:
# Time complexity: O(n) where n is the length of arr. We traverse the arr
# array once to create the set and then once more to count the elements.
# Space complexity: O(n) for storing the set of elements.
