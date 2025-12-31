# Given a binary array nums, return the maximum length of a contiguous
# subarray with an equal number of 0 and 1.


# Example 1:

# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an
# equal number of 0 and 1.
# Example 2:

# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray
# with equal number of 0 and 1.
# Example 3:

# Input: nums = [0,1,1,1,1,1,0,0,0]
# Output: 6
# Explanation: [1,1,1,0,0,0] is the longest contiguous subarray
# with equal number of 0 and 1.

from collections import defaultdict


class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        answer = 0
        seen = defaultdict(int)
        sum_tracker = 0
        seen[0] = -1  # Tracks sum_tracker:idx

        for i in range(len(nums)):
            if nums[i] == 1:
                sum_tracker += 1
            else:
                sum_tracker -= 1

            if sum_tracker in seen:
                answer = max(answer, i - seen[sum_tracker])
            else:
                seen[sum_tracker] = i

        return answer


# Explanation:
# - Treat 1 as +1 and 0 as -1, so equal zeros and ones means prefix sum repeats.
# - In other words, when the same cumulative sum appears again, the subarray
#   between the two indices has equal numbers of 0s and 1s.
# - Store the first index where each prefix sum appears.
# - The distance between repeated sums gives a candidate length; keep the max.

# Complexity Analysis:
# Time complexity: O(n) - We traverse the array once, performing O(1) operations
# for each element. Thus, the overall time complexity is linear with respect to
#  the size of the input array.
# Space complexity: O(n) - In the worst case, we may store all unique
# cumulative sums in the hashmap. Therefore, the space complexity is also linear
# with respect to the size of the input array.
