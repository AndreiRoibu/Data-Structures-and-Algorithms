# You are given an array of integers nums, there is a sliding window of size k
# which is moving from the very left of the array to the very right. You can
# only see the k numbers in the window. Each time the sliding window moves
# right by one position.

# Return the max sliding window.


# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = []
        queue = deque()

        for i in range(len(nums)):
            # Monotonic decreasing function
            # - queue[0] is max
            # - elements smaller than current go.
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            # We add at our current
            queue.append(i)

            # if Max is out of window, pop it
            if queue[0] + k == i:
                queue.popleft()

            # Because we iterate, only add answer after reaching K
            if i >= k - 1:
                ans.append(nums[queue[0]])

        return ans


# Complexity Analysis:
# Time complexity : O(N) - Each element is pushed and popped at most once from
# the deque.
# Space complexity : O(K) - The size of the deque can go up to K in the worst case
# when the elements are in increasing order, where K is the size of the sliding
# window.

# >> Note to self: I tried the max function on slices, but it resulted in timeout
# for large inputs, because that would be O(N*K) time complexity. The O(N*K)
# complexity arises because for each of the N elements, we would be computing
# the maximum of a subarray of size K, leading to K comparisons for each of the
# N elements.
