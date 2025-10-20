# Stacks and Queues

## 1.1 Introduction to Stacks

A stack is an ordered collection of elements where elements are only added and removed from the same end. Another term used to describe stacks is LIFO, which stands for last in, first out. The last (most recent) element placed inside is the first element to come out.

In Python, you can just use a list stack = [] and use stack.append(element) and stack.pop(). In fact, any dynamic array can implement a stack. Typically, inserting into a stack is called pushing and removing from a stack is called popping. Stacks will usually also come with operations like peek, which means looking at the element at the top of the stack.

The time complexity of stack operations is dependent on the implementation. If you use a dynamic array, which is the most common and easiest way, then the time complexity of your operations is the same as that of a dynamic array. O(1) push, pop, and random access, and O(n) search. Sometimes, a stack may be implemented with a linked list with a tail pointer.

The characteristic that makes something a "stack" is that you can only add and remove elements from the same end. It doesn't matter how you implement it, a "stack" is just an abstract interface.

Stacks and recursion are very similar. This is because recursion is actually done using a stack. Function calls are pushed on a stack. The call at the top of the stack at any given moment is the "active" call. On a return statement or the end of the function being reached, the current call is popped off the stack.

For algorithm problems, a stack is a good option whenever you can recognize the LIFO pattern. Usually, there will be some component of the problem that involves elements in the input interacting with each other. Interacting could mean matching elements together, querying some property such as "how far is the next largest element", evaluating a mathematical equation given as a string, just comparing elements against each other, or any other abstract interaction. Sometimes, the LIFO property is hard to see, but we'll make sure to talk about how we recognize it in this chapter.

```python
# Declaration: we will just use a list
stack = []

# Pushing elements:
stack.append(1)
stack.append(2)
stack.append(3)

# Popping elements:
stack.pop() # 3
stack.pop() # 2

# Check if empty
not stack # False

# Check element at top
stack[-1] # 1

# Get size
len(stack) # 1
```

## 1.2 Introduction to Queues

While a stack followed a LIFO pattern, a queue follows FIFO (first in first out). In a stack, elements are added and removed from the same side. In a queue, elements are added and removed from opposite sides. Like with a stack, there are multiple ways to implement a queue, but the important thing that defines it is the abstract interface of adding and removing from opposite sides.

Queues are trickier to implement than stacks if you want to maintain good performance. Like a stack, you could just use a dynamic array, but operations on the front of the array (adding or removal) are O(n), where n is the size of the array. Adding to a queue is called enqueue and deletions are called dequeue. If you want these operations to be O(1), you'll need a more sophisticated implementation.

One way to implement an efficient queue is by using a doubly linked list. Recall that with a doubly linked list, if you have the pointer to a node, you can add or delete at that location in O(1). A doubly linked list that maintains pointers to the head and tail (both ends, usually with sentinel nodes) can implement an efficient queue.

There is also a data structure called a deque, short for double-ended queue, and pronounced "deck". In a deque, you can add or delete elements from both ends. A normal queue designates adding to one end and deleting to another end.

The most common use of a queue is to implement an algorithm called breadth-first search (BFS). Outside of BFS, unlike stack, there aren't many problems whose main focus is a queue.

```python
# Declaration: we will use deque from the collections module
import collections
queue = collections.deque()

# If you want to initialize it with some initial values:
queue = collections.deque([1, 2, 3])

# Enqueueing/adding elements:
queue.append(4)
queue.append(5)

# Dequeuing/removing elements:
queue.popleft() # 1
queue.popleft() # 2

# Check element at front of queue (next element to be removed)
queue[0] # 3

# Get size
len(queue) # 3
```

# 2. String Problems

Normally, string questions that can utilize a stack will involve iterating over the string and putting characters into the stack, and comparing the top of the stack with the current character at each iteration. Stacks are useful for string matching because it saves a "history" of the previous characters.

## 2.1. Example 1 - Valid Parantheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The string is valid if all open brackets are closed by the same type of closing bracket in the correct order, and each closing bracket closes exactly one open bracket.

For example, s = "({})" and s = "(){}[]" are valid, but s = "(]" and s = "({)}" are not valid.

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {"(": ")", "[": "]", "{": "}"}

        for c in s:
            if c in matching: # if c is an opening bracket
                stack.append(c)
            else:
                if not stack:
                    return False

                previous_opening = stack.pop()
                if matching[previous_opening] != c:
                    return False

        return not stack
```

Because the stack's push and pop operations are O(1), this gives us a time complexity of O(n), where n is the size of the input array. This is because each element can only be pushed or popped once. The space complexity is also O(n) because the stack's size can grow linearly with the input size.

## 2.2. Example 2 - Remove all Adjacent Duplicates In String

You are given a string s. Continuously remove duplicates (two of the same character beside each other) until you can't anymore. Return the final string after this.

For example, given s = "abbaca", you can first remove the "bb" to get "aaca". Next, you can remove the "aa" to get "ca". This is the final answer.

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)
```

Remember that stacks are defined by their interface - we just need to add and remove from the same end. Because strings in C++ are mutable, we can just use a string as a stack and return the answer directly. In Java, we can use StringBuilder as a stack as its a convenient way to get the answer in string format at the end. This algorithm has a time and space complexity of O(n), where n is the length of the input. This is because the stack operations in all implementations above are O(1), and the stacks themselves can grow to O(n) size.

## 2.3. Example 3 - Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

For example, given s = "ab#c" and t = "ad#c", return true. Because of the backspace, the strings are both equal to "ac".

```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            stack = []
            for c in s:
                if c != "#":
                    stack.append(c)
                elif stack:
                    stack.pop()

            return "".join(stack)

        return build(s) == build(t)
```

Just like in the previous approaches, this approach has a time and space complexity linear with the input sizes, because our stack implementations are efficient.

# 3. Queue Problems

## 3.1. Example 1 - Number of Recent Calls

Implement the RecentCounter class. It should support ping(int t), which records a call at time t, and then returns an integer representing the number of calls that have happened in the range [t - 3000, t]. Calls to ping will have increasing t.

```python
from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()

        self.queue.append(t)
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
```

In Python, we're using collections.deque to implement the queue. This data structure allows us to perform dequeue operations from the front in O(1).

# 4. Monotonic

Monotonic: (of a function or quantity) varying in such a way that it either never decreases or never increases.

A monotonic stack or queue is one whose elements are always sorted. It can be sorted either ascending or descending, depending on the algorithm. Monotonic stacks and queues maintain their sorted property by removing elements that would violate the property before adding new elements. For example, let's say you had a monotonically increasing stack, currently stack = [1, 5, 8, 15, 23]. You want to push 14 onto the stack. To maintain the sorted property, we need to first pop the 15 and 23 before pushing the 14 - after the push operation, we have stack = [1, 5, 8, 14].

Here's some pseudocode for maintaining a monotonic increasing stack over an input array:

```
Given an integer array nums

stack = []
for num in nums:
    while stack.length > 0 AND stack.top >= num:
        stack.pop()
    // Between the above and below lines, do some logic depending on the problem
    stack.push(num)

```

As we discussed earlier in the sliding window chapter, despite the nested loop, the time complexity is still O(n), where n is the length of the array, because the inner while loop can only iterate over each element once across all for loop iterations, making the for loop iterations amortized O(1).

Monotonic stacks and queues are useful in problems that, for each element, involves finding the "next" element based on some criteria, for example, the next greater element. They're also good when you have a dynamic window of elements and you want to maintain knowledge of the maximum or minimum element as the window changes. In more advanced problems, sometimes a monotonic stack or queue is only one part of the algorithm. Let's look at some examples.

## 4.1. Example 1 - Daily Temperatures

Given an array of integers temperatures that represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day that is warmer, have answer[i] = 0 instead.

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)

        return answer
```

## 4.2. Example 2 - Sliding Window Maximum

Given an integer array nums and an integer k, there is a sliding window of size k that moves from the very left to the very right. For each window, find the maximum element in the window.

For example, given nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3, return [3, 3, 5, 5, 6, 7]. The first window is [1, 3, -1, -3, 5, 3, 6, 7] and the last window is [1, 3, -1, -3, 5, 3, 6, 7]

Note: this problem is significantly more difficult than any problem we have looked at so far. Don't be discouraged if you are having trouble understanding the solution.

```python
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = deque()
        for i in range(len(nums)):
            # maintain monotonic decreasing.
            # all elements in the deque smaller than the current one
            # have no chance of being the maximum, so get rid of them
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

            queue.append(i)

            # queue[0] is the index of the maximum element.
            # if queue[0] + k == i, then it is outside the window
            if queue[0] + k == i:
                queue.popleft()

            # only add to the answer once our window has reached size k
            if i >= k - 1:
                ans.append(nums[queue[0]])

        return ans
```

This problem is quite difficult - try your best to understand the solution as it is a good demonstration of how powerful a deque is - the time complexity is O(n), where n is the size of nums! The space complexity is O(k), since the deque can't grow beyond that size. To summarize:

- We use a monotonic decreasing deque, which implies that the first element is the maximum.
- Once the maximum element is too far to stay in the window we remove it from the deque, and the next greatest element moves to position 0.
- To maintain the decreasing order, we remove elements from the deque that are smaller than the elements being added.

## 4.3. Example 3 - Longest Continous Subarray With Absolute Diff Less Than or Equal to Limit

Given an array of integers nums and an integer limit, return the size of the longest subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

```python
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increasing = deque()
        decreasing = deque()
        left = ans = 0

        for right in range(len(nums)):
            # maintain the monotonic deques
            while increasing and increasing[-1] > nums[right]:
                increasing.pop()
            while decreasing and decreasing[-1] < nums[right]:
                decreasing.pop()

            increasing.append(nums[right])
            decreasing.append(nums[right])

            # maintain window property
            while decreasing[0] - increasing[0] > limit:
                if nums[left] == decreasing[0]:
                    decreasing.popleft()
                if nums[left] == increasing[0]:
                    increasing.popleft()
                left += 1

            ans = max(ans, right - left + 1)

        return ans
```

With efficient queues, this algorithm has a time and space complexity of O(n) as each for loop iteration is amortized O(1) and the deques can grow to size n, where n is the size of nums.
