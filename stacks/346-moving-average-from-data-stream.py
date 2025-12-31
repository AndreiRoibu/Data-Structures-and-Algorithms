# Given a stream of integers and a window size, calculate the moving average of
# all integers in the sliding window.

# Implement the MovingAverage class:

# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of
# the stream.


# Example 1:

# Input
# ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5]]
# Output
# [null, 1.0, 5.5, 4.66667, 6.0]

# Explanation
# MovingAverage movingAverage = new MovingAverage(3);
# movingAverage.next(1); // return 1.0 = 1 / 1
# movingAverage.next(10); // return 5.5 = (1 + 10) / 2
# movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
# movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3


# Constraints:

# 1 <= size <= 1000
# -105 <= val <= 105
# At most 104 calls will be made to next.

from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.count += 1

        if self.count > self.size:
            dropped = self.queue.popleft()
            denominator = self.size
        else:
            dropped = 0
            denominator = self.count

        self.window_sum += val - dropped

        return self.window_sum / denominator


# Explanation:
# - Keep a queue of the last `size` values and a running sum.
# - When the window exceeds the size, drop the oldest value.
# - Divide the running sum by the current window length.

# Complexity Analysis:
# Time complexity: O(1) for each call to next.
# Space complexity: O(size) to store the elements in the queue.
