# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# Example 2:

# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15


# Constraints:

# 1 <= nums.length <= 3 * 104
# nums[i] is either 0 or 1.
# 0 <= goal <= nums.length

from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        """Finds the number of continuous subarrays that sum up to a given goal.

        This solution uses the "Prefix Sum" technique combined with a Hash Map.
        Instead of checking every possible subarray (which is too slow), we keep a
        running sum of the array. At each step, we check if there was a previous
        running sum that, if chopped off from our current sum, leaves us with
        exactly our target `goal`.

        Args:
            nums (List[int]): A binary array containing only 0s and 1s.
            goal (int): The target sum we want our subarrays to equal.

        Returns:
            int: The total number of subarrays whose sum is exactly `goal`.

        Time Complexity:
            O(N): Where N is the length of `nums`.
            We loop through the array exactly once. Calculating the sum and
            looking up values in our hash map (`freq`) both take O(1) time on average.
            Therefore, the total time spent scales linearly with the size of the input.

        Space Complexity:
            O(N): In the worst case, every single prefix sum we calculate is unique
            (e.g., if the array is all 1s). Our dictionary `freq` will need to store
            a count for every single one of those unique prefix sums, scaling linearly.
        """
        # Keeps track of how many valid subarrays we've found
        total_count = 0

        # Keeps a running total of the sum from the beginning of the array to our current index
        current_sum = 0

        # A hash map (dictionary) to store how many times we've seen a specific prefix sum.
        # It defaults to 0 if a sum hasn't been seen yet.
        freq = defaultdict(int)

        # Iterate through the array one number at a time
        for num in nums:
            # Add the current number to our running total
            current_sum += num

            # Scenario 1: The subarray from the VERY BEGINNING up to here equals the goal.
            # We count this as 1 valid subarray.
            if current_sum == goal:
                total_count += 1

            # Scenario 2: A subarray SOMEWHERE IN THE MIDDLE equals the goal.
            # We check if there is any earlier prefix sum that we can subtract
            # from our current sum to get exactly the 'goal'.
            tmp = current_sum - goal

            # If we have seen 'tmp' before, it means the subarray between that old
            # prefix sum and our current position equals 'goal'.
            if tmp in freq:
                # Add the number of times we've seen that old sum to our total count
                total_count += freq[tmp]

            # Record that we have seen our current running total one more time
            freq[current_sum] += 1

        # Return the final tally of all valid subarrays
        return total_count


class Solution2:
    def sliding_window_at_most(self, nums: list[int], goal: int) -> int:
        """Helper function to count the number of subarrays with sum at most the given goal.

        Args:
            nums (List[int]): The binary array.
            goal (int): The maximum allowed sum for the subarrays.

        Returns:
            int: The total count of valid subarrays where the sum <= goal.
        """
        # If the goal is negative, it's impossible to have a valid subarray
        # because the array only contains 0s and 1s.
        if goal < 0:
            return 0

        left = 0
        current_sum = 0
        total_count = 0

        # Iterate through the array using a sliding window approach
        for right in range(len(nums)):
            # Expand the window by adding the current right element
            current_sum += nums[right]

            # Adjust the window by moving the start pointer to the right
            # until the sum becomes less than or equal to the goal.
            while left <= right and current_sum > goal:
                current_sum -= nums[left]
                left += 1

            # Update the total count by adding the length of the current subarray.
            # Why length? Because if the window [left...right] is valid,
            # every subarray ending at 'right' within this window is also valid!
            total_count += right - left + 1

        return total_count

    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        """Finds the number of continuous subarrays that sum up to exactly a given goal.

        This uses the Sliding Window "At Most" trick. Since the array only contains
        non-negative numbers, finding the exact sum is mathematically equivalent to:
        (Subarrays with sum <= goal) minus (Subarrays with sum <= goal - 1).

        Args:
            nums (List[int]): A binary array containing only 0s and 1s.
            goal (int): The exact target sum we want our subarrays to equal.

        Returns:
            int: The total number of subarrays whose sum is exactly `goal`.

        Time Complexity:
            O(N): Where N is the length of `nums`.
            We call the helper function twice. Inside the helper function, both the `left`
            and `right` pointers only move forward. Each element is visited at most twice
            (once by right, once by left), making it O(N). Two passes of O(N) is still O(N).

        Space Complexity:
            O(1): We only use a few integer variables (`left`, `right`, `current_sum`,
            `total_count`) to keep track of our window. No extra data structures are used,
            meaning space is constant regardless of input size.
        """
        # Calculate exactly 'goal' by subtracting 'at most goal - 1' from 'at most goal'
        return self.sliding_window_at_most(nums, goal) - self.sliding_window_at_most(nums, goal - 1)
