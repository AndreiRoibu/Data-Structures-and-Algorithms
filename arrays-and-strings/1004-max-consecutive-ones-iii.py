# Given a binary array nums and an integer k, return the maximum number of
# consecutive 1's in the array if you can flip at most k 0's.

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = curr = ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


# Explanation:
# - Expand a sliding window while tracking how many zeros are inside it.
# - If zeros exceed k, shrink from the left until the window is valid again.
# - Track the maximum window length seen.

# Complexity Analysis
# ----------------------------
# Time Complexity: O(N), where N is the length of nums. Each element is visited
# at most twice, once by the right pointer and once by the left pointer.
# Space Complexity: O(1), we are using only a constant amount of extra space.
# ----------------------------
