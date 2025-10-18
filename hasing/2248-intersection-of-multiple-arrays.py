# Given a 2D integer array nums where nums[i] is a non-empty array of distinct
# positive integers, return the list of integers that are present in each
# array of nums sorted in ascending order.


# Example 1:

# Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
# Output: [3,4]
# Explanation:
# The only integers present in each of nums[0] = [3,1,2,4,5],
# nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].
# Example 2:

# Input: nums = [[1,2,3],[4,5,6]]
# Output: []
# Explanation:
# There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].


# Constraints:

# 1 <= nums.length <= 1000
# 1 <= sum(nums[i].length) <= 1000
# 1 <= nums[i][j] <= 1000
# All the values of nums[i] are unique.


class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        original_set = set(nums[0])
        for idx in range(1, len(nums)):
            original_set = original_set & set(nums[idx])

        return sorted(original_set)


# Complexity Analysis:
# Time Complexity: O(m⋅(n+logm)) - where n is the number of lists and m is the
# average number of elements in each list.
# Space Complexity: O(n⋅m) - in the worst case, when all elements are unique
# across all lists.

from collections import defaultdict  # noqa: E402


class Solution2:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        counts = defaultdict(int)
        for arr in nums:
            for x in arr:
                counts[x] += 1

        n = len(nums)
        ans = []
        for key in counts:
            if counts[key] == n:
                ans.append(key)

        return sorted(ans)


# Complexity Analysis:
# Time Complexity: O(m⋅(n+logm)) - where n is the number of lists and m is the
# average number of elements in each list.
# Space Complexity: O(n⋅m) - in the worst case, when all elements are unique
# across all lists.
