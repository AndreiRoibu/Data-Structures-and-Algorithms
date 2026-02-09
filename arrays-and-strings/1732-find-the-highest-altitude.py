# There is a biker going on a road trip. The road trip consists of n + 1 points
# at different altitudes. The biker starts his trip on point 0 with altitude
# equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain
# in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the
# highest altitude of a point.


# Example 1:

# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
# Example 2:

# Input: gain = [-4,-3,-2,-1,4,3,2]
# Output: 0
# Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.


# Constraints:

# n == gain.length
# 1 <= n <= 100
# -100 <= gain[i] <= 100

# Hint 1
# Let's note that the altitude of an element is the sum of gains of all the
# elements behind it
# Hint 2
# Getting the altitudes can be done by getting the prefix sum array of the
# given array


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitude = 0
        ans = 0
        for elem in gain:
            altitude += elem
            ans = max(ans, altitude)
        return ans


# - **Summary explainer (for future reference)**
#   - Start at altitude 0.
#   - Iterate through `gain`, updating a running `altitude` by adding each gain
#       value.
#   - After each update, compare `altitude` with `ans` (the maximum altitude
#       seen so far) and update `ans` if needed.
#   - Return `ans` as the highest altitude reached.

# - **Time Complexity: O(n)**
#   - `n = len(gain)`.
#   - You loop through the `gain` array once.
#   - Each iteration does O(1) work (simple arithmetic and `max`), so total time
#    is linear.

# - **Space Complexity: O(1)**
#   - You use a constant number of variables: `altitude` and `ans`.
#   - No extra data structures grow with input size.
#   - Space usage stays the same regardless of how large `gain` is.
