# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have
# to wait after the ith day to get a warmer temperature. If there is no
# future day for which this is possible, keep answer[i] == 0 instead.


# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]


# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        len_temp = len(temperatures)
        answer = [0] * len_temp

        for i in range(len_temp):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)

        return answer


# Complexity Analysis
# Time complexity : O(N) - Each element is pushed and popped at most once from
# the stack.
# Space complexity : O(N) - The size of the stack can go up to N in the worst case
# when the temperatures are in decreasing order.
