# Given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# return the minimum integer common to both arrays. If there is no common
# integer amongst nums1 and nums2, return -1.

# Note that an integer is said to be common to nums1 and nums2 if both arrays
# have at least one occurrence of that integer.


# Example 1:

# Input: nums1 = [1,2,3], nums2 = [2,4]
# Output: 2
# Explanation: The smallest element common to both arrays is 2, so we return 2.
# Example 2:

# Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
# Output: 2
# Explanation: There are two common elements in the array 2 and 3 out of which 2
# is the smallest, so 2 is returned.


# Constraints:

# 1 <= nums1.length, nums2.length <= 105
# 1 <= nums1[i], nums2[j] <= 109
# Both nums1 and nums2 are sorted in non-decreasing order.

# Hint 1
# Try to use a set.

# Hint 2
# Otherwise, try to use a two-pointer approach.


class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        nums1 = set(nums1)  # pyright: ignore[reportAssignmentType]

        for x in nums2:
            if x in nums1:
                return x

        return -1


# Explanation:
# - Convert nums1 to a set for O(1) average time complexity lookups.
# - Iterate through nums2 and return the first element found in the set.
# - If no common element is found, return -1.

# Complexity Analysis:
# Time complexity: O(n + m), where n and m are the lengths of nums1 and nums2
# respectively. Creating the set takes O(n) time, and checking each element of nums2
# takes O(m) time.
# Space complexity: O(n), for storing the elements of nums1 in a set.


class Solution2:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:  # pyright: ignore[reportUndefinedVariable]
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                return nums1[i]

        return -1


# Explanation:
# - Use two pointers to traverse both sorted arrays.
# - Increment the pointer of the array with the smaller current element.
# - If elements are equal, return the common element.
# - If the end of either array is reached without finding a common element, return -1.

# Complexity Analysis:
# Time complexity: O(n + m), where n and m are the lengths of nums1 and nums2
# respectively. Each element from both arrays is processed at most once.
# Space complexity: O(1), as no additional space is used that scales with input size.
