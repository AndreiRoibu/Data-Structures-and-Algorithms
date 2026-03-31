# Implement a last-in-first-out (LIFO) stack using only two queues. The
# implemented stack should support all the functions of a normal stack
# (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:

# You must use only standard operations of a queue, which means that only push
# to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may
# simulate a queue using a list or deque (double-ended queue) as long as you
# use only a queue's standard operations.


# Example 1:

# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False


# Constraints:

# 1 <= x <= 9
# At most 100 calls will be made to push, pop, top, and empty.
# All the calls to pop and top are valid.


# Follow-up: Can you implement the stack using only one queue?

import collections


class MyStack:
    """
    A class that implements a Last-In-First-Out (LIFO) stack using a single Queue.

    Summary:
        This implementation strictly adheres to standard queue operations (FIFO).
        To achieve LIFO behavior (Stack), it rotates the queue during `pop` and `top`
        operations by repeatedly removing from the front and appending to the back,
        making the last-added element accessible.

    Space Complexity:
        O(N): Where N is the number of elements in the stack. All elements are
        stored in a single `collections.deque`.
    """

    def __init__(self):
        """
        Initializes the stack object with an empty queue.

        Time Complexity: O(1)
        """
        self.queue = collections.deque()

    def push(self, x: int) -> None:
        """
        Pushes element x onto the stack by enqueuing it to the back.

        Args:
            x (int): The integer element to be pushed onto the stack.

        Time Complexity: O(1)
        """
        # Standard queue operation: push to the back.
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on the top of the stack and returns it.

        Returns:
            int: The element that was at the top of the stack (most recently pushed).

        Time Complexity: O(N), where N is the current size of the queue.
        """
        len_queue = len(self.queue)

        # Dequeue and enqueue (rotate) all elements one by one.
        for idx in range(len_queue):
            x = self.queue.popleft()

            # If it's not the very last element in our iteration (which is the "top" of our stack),
            # we put it back at the end of the queue.
            if idx != len_queue - 1:
                self.queue.append(x)

        # The last element extracted is NOT appended back, effectively removing it.
        return x  # pyright: ignore[reportPossiblyUnboundVariable]

    def top(self) -> int:
        """
        Returns the element on the top of the stack without removing it.

        Returns:
            int: The element at the top of the stack.

        Time Complexity: O(N), where N is the current size of the queue.
        """
        # To find the top without removing it, we must rotate the ENTIRE queue.
        for _ in range(len(self.queue)):
            x = self.queue.popleft()
            self.queue.append(x)

        # The variable 'x' will hold the value of the last extracted (and re-appended) element,
        # which represents the top of the stack.
        return x  # pyright: ignore[reportPossiblyUnboundVariable]

    def empty(self) -> bool:
        """
        Returns True if the stack is empty, False otherwise.

        Returns:
            bool: True if empty, False if not.

        Time Complexity: O(1)
        """
        return not self.queue


class MyStack2:
    """
    A class that implements a Last-In-First-Out (LIFO) stack using a single Queue.

    Summary:
        This implementation strictly adheres to standard queue operations (FIFO).
        To achieve LIFO behavior while keeping `pop` and `top` operations O(1),
        it performs a rotation immediately upon pushing a new element.
        When a new element is appended to the back of the queue, the remaining elements
        are dequeued from the front and enqueued to the back. This effectively places
        the newly added element at the front of the queue, ready to be popped or accessed instantly.

    Space Complexity:
        O(N): Where N is the number of elements in the stack. All elements are
        stored in a single `collections.deque`.
    """

    def __init__(self):
        """
        Initializes the stack object with an empty queue.

        Time Complexity: O(1)
        """
        self.queue = collections.deque()

    def push(self, x: int) -> None:
        """
        Pushes element x onto the stack and rotates the queue so it becomes the new front.

        Args:
            x (int): The integer element to be pushed onto the stack.

        Time Complexity: O(N), where N is the current size of the queue after appending.
        """
        # 1. Add the new element to the back of the queue (Standard Queue operation)
        self.queue.append(x)

        # 2. Rotate all the *other* elements in the queue.
        # We loop exactly (length - 1) times to move all older elements to the back,
        # ensuring the newly added element 'x' ends up at the very front of the queue.
        for _ in range(len(self.queue) - 1):
            # Pop the oldest element from the front and append it to the back.
            # Note: Overwriting 'x' here is harmless, as 'x' is just a local variable
            # in this loop and the queue already safely contains the original value of 'x'.
            x = self.queue.popleft()
            self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on the top of the stack and returns it.

        Returns:
            int: The element that was at the top of the stack (most recently pushed).

        Time Complexity: O(1)
        """
        # Because we rotated the queue during the 'push' operation,
        # the "top" of our stack is conveniently sitting at the front of our queue.
        # Standard queue operation: pop from front.
        return self.queue.popleft()

    def top(self) -> int:
        """
        Returns the element on the top of the stack without removing it.

        Returns:
            int: The element at the top of the stack.

        Time Complexity: O(1)
        """
        # The "top" of our stack is sitting at the front of our queue.
        # Standard queue operation: peek at front.
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns True if the stack is empty, False otherwise.

        Returns:
            bool: True if empty, False if not.

        Time Complexity: O(1)
        """
        # Standard check to see if the queue is empty.
        return not self.queue
