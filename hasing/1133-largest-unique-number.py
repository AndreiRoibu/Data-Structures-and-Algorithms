# Given an integer array nums, return the largest integer that only
# occurs once. If no integer occurs once, return -1.


# Example 1:

# Input: nums = [5,7,3,9,4,9,8,3,1]
# Output: 8
# Explanation: The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.
# Example 2:

# Input: nums = [9,9,8,8]
# Output: -1
# Explanation: There is no number that occurs only once.

from collections import OrderedDict, defaultdict


class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        answer = -1
        for val, count in counts.items():
            if count == 1:
                answer = max(answer, val)

        return answer


# Complexity Analysis
# Time Complexity: O(N), where N is the length of the input array nums. We
# traverse the array once to count the occurrences of each number, and then
# traverse the counts dictionary to find the largest unique number.
# Space Complexity: O(N) in the worst case, when all elements are unique.


class Solution2:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        sorted_map = OrderedDict(sorted(counts.items(), reverse=True))

        for num, freq in sorted_map.items():
            if freq == 1:
                return num

        return -1


# Complexity Analysis
# Time Complexity: O(N log N), where N is the length of the input array nums. We
# traverse the array once to count the occurrences of each number, and then
# sort the unique numbers which takes O(N log N) time.
# Space Complexity: O(N) in the worst case, when all elements are unique.
