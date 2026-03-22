# Implement a first in first out (FIFO) queue using only two stacks. The
# implemented queue should support all the functions of a normal queue (push,
# peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:

# You must use only standard operations of a stack, which means only push to
# top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may
# simulate a stack using a list or deque (double-ended queue) as long as you
# use only a stack's standard operations.


# Example 1:

# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]

# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false


# Constraints:

# 1 <= x <= 9
# At most 100 calls will be made to push, pop, peek, and empty.
# All the calls to pop and peek are valid.


# Follow-up: Can you implement the queue such that each operation is amortized
# O(1) time complexity? In other words, performing n operations will take
# overall O(n) time even if one of those operations may take longer.


class MyQueue:
    """
    A First-In-First-Out (FIFO) queue data structure.

    Explainer:
    This solution utilizes a single Python list (`stack`) to store the elements.
    It mimics a queue by appending new elements to the end of the list (pushing)
    and removing elements from the very beginning of the list using `pop(0)`.
    While named `stack`, it is effectively being used as a dynamic array where
    we extract from the front to maintain the FIFO property.

    Complexity Analysis:
        Time Complexity:
            - push: O(1) appending to the end of a list is an O(1) operation.
            - pop: O(N) where N is the number of elements in the queue. `pop(0)`
                   forces Python to shift all remaining elements in the list one
                   index to the left, which takes linear time.
            - peek: O(1) accessing the first index `[0]` takes constant time.
            - empty: O(1) checking the boolean value of a list takes constant time.
        Space Complexity: O(N), where N is the number of elements stored in the
                          queue, as we maintain them inside the `stack` list.
    """

    def __init__(self):
        # Initialize an empty list to store the queue elements
        self.stack = []

    def push(self, x: int) -> None:
        """
        Pushes element x to the back of the queue.
        """
        # Append adds the element to the end of the list (back of the queue)
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from the front of the queue and returns it.
        """
        # pop(0) removes and returns the element at the 0th index (front of the queue).
        # Note: This operation takes O(N) time because it shifts all other elements.
        return self.stack.pop(0)

    def peek(self) -> int:
        """
        Returns the element at the front of the queue without removing it.
        """
        # Return the element at the 0th index without modifying the list
        return self.stack[0]

    def empty(self) -> bool:
        """
        Returns true if the queue is empty, false otherwise.
        """
        # In Python, an empty list evaluates to False, so 'not self.stack'
        # returns True when empty, and False when it contains elements.
        return not self.stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


class MyQueue2:
    """
    A First-In-First-Out (FIFO) queue implemented using two stacks.

    Explainer:
    This solution uses two stacks (lists in Python) to simulate a queue.
    - `in_stack` is used strictly to collect incoming elements (pushes).
    - `out_stack` is used to serve outgoing elements (pops and peeks).
    Because a stack is Last-In-First-Out (LIFO), popping everything from `in_stack`
    and pushing it into `out_stack` reverses the order of the elements. The oldest
    element ends up at the top of `out_stack`, perfectly simulating a queue's FIFO behavior.
    To maintain efficiency, we only move elements when `out_stack` is completely empty.

    Complexity Analysis:
        Time Complexity:
            - push(): O(1) - Appending to a list is a constant time operation.
            - pop(): Amortized O(1) - In the worst case (when out_stack is empty), this takes
                     O(N) time to move elements from in_stack. However, each element is moved
                     exactly once, making the average (amortized) time per operation O(1).
            - peek(): Amortized O(1) - Same logic as pop().
            - empty(): O(1) - Checking if two lists are empty takes constant time.
        Space Complexity: O(N), where N is the total number of elements currently stored
                          in the queue across both stacks.
    """

    def __init__(self):
        # Stack to hold all newly pushed elements
        self.in_stack = []
        # Stack to hold elements ready to be popped or peeked in FIFO order
        self.out_stack = []

    def push(self, x: int) -> None:
        """Pushes element x to the back of the queue."""
        # Always add new elements to the in_stack
        self.in_stack.append(x)

    def pop(self) -> int:
        """Removes the element from the front of the queue and returns it."""
        # Ensure out_stack has the oldest elements ready
        self._move_if_needed()
        # Remove and return the top element of out_stack (the front of the queue)
        return self.out_stack.pop()

    def peek(self) -> int:
        """Returns the element at the front of the queue without removing it."""
        # Ensure out_stack has the oldest elements ready
        self._move_if_needed()
        # Return the top element of out_stack without removing it
        return self.out_stack[-1]

    def empty(self) -> bool:
        """Returns true if the queue is empty, false otherwise."""
        # The queue is only empty if there are no elements in either stack
        return not self.in_stack and not self.out_stack

    def _move_if_needed(self) -> None:
        """
        Helper method: Transfers elements from in_stack to out_stack if out_stack is empty.

        Do not transfer elements every time.
        Only transfer from in_stack to out_stack when out_stack is empty to maintain
        amortized O(1) time complexity.
        """
        # If out_stack still has elements, they are correctly ordered, so do nothing
        if not self.out_stack:
            # Pop all elements from in_stack and append them to out_stack, reversing their order
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
