# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.


# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2


# Constraints:

# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.


# Hint 1
# Consider each node in the stack having a minimum value. (Credits to
# @aakarshmadhavan)


class MinStack:
    """A stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Explainer:
        This implementation achieves O(1) time complexity for all operations by storing pairs
        of values in a single stack. Every time an element is pushed, we store it as a list:
        `[actual_value, current_minimum_value]`. By taking a "snapshot" of the minimum value
        at the time each element is added, we can instantly retrieve the minimum without
        scanning the stack. When an element is popped, the previous minimum is naturally restored.

    Overall Space Complexity:
        O(N) where N is the maximum number of elements in the stack at any given time,
        since we store an auxiliary minimum value alongside every pushed element.
    """

    def __init__(self):
        """Initializes the stack object.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Main stack to store pairs of [value, current_min]
        self.stack = []

    def push(self, val: int) -> None:
        """Pushes the element val onto the stack.

        Explainer:
            Checks if the stack is empty to determine the new minimum. If empty,
            the new value is the minimum. Otherwise, it compares the new value with
            the current minimum (stored in the second index of the top element)
            to find the new minimum.

        Args:
            val (int): The value to push onto the stack.

        Time Complexity: O(1)
        Space Complexity: O(1) auxiliary space per operation.
        """
        # If the stack is empty, the newly pushed value is automatically the minimum.
        # If the stack is not empty, the current minimum is the smaller of the new value
        # or the minimum value stored at the top of the stack.
        min_val = val if not self.stack else min(val, self.stack[-1][1])

        # Append both the value and the minimum at this level as a list.
        self.stack.append([val, min_val])

    def pop(self) -> None:
        """Removes the element on the top of the stack.

        Explainer:
            Pops the top element from the underlying list. Since the minimum
            value at each state is stored alongside the value, removing the top element
            automatically restores the previous minimum.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Remove the last appended [val, min_val] pair.
        self.stack.pop()

    def top(self) -> int:
        """Gets the top element of the stack.

        Explainer:
            Accesses the last element in the stack and returns its first item (the actual value).

        Returns:
            int: The actual value at the top of the stack.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # self.stack[-1] gets the top pair, [0] gets the actual value.
        return self.stack[-1][0]

    def getMin(self) -> int:
        """Retrieves the minimum element in the stack.

        Explainer:
            Accesses the last element in the stack and returns its second item
            (the tracked minimum value up to that point).

        Returns:
            int: The minimum value currently in the stack.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # self.stack[-1] gets the top pair, [1] gets the tracked minimum value.
        return self.stack[-1][1]
