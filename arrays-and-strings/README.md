# Common Techniques and Patterns

<!-- vscode-markdown-toc -->
* 1. [Two Pointers](#TwoPointers)
	* 1.1. [Pointers at the Edges](#PointersattheEdges)
	* 1.2. [Move along both inputs simultaneously until all elements have been checked](#Movealongbothinputssimultaneouslyuntilallelementshavebeenchecked)
* 2. [Sliding Window](#SlidingWindow)
	* 2.1. [Subarrays](#Subarrays)
	* 2.2. [Using Sliding Window](#UsingSlidingWindow)
	* 2.3. [Implementation Examples](#ImplementationExamples)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

##  1. <a name='TwoPointers'></a>Two Pointers

Two pointers is an extremely common technique used to solve array and string problems. It involves having two integer variables that both move along an iterable. This means we will have two integers, usually named something like `i` and `j`, or `left` and `right` which each represent an index of the array or string.

###  1.1. <a name='PointersattheEdges'></a>Pointers at the Edges

Start the pointers at the edges of the input. Move them towards each other until they meet.

Converting this idea into instructions:
1. Start one pointer at the first index 0 and the other pointer at the last index input.length - 1.
2. Use a while loop until the pointers are equal to each other.
3. At each iteration of the loop, move the pointers towards each other. This means either increment the pointer that started at the first index, decrement the pointer that started at the last index, or both. Deciding which pointers to move will depend on the problem we are trying to solve.

Here's some pseudocode illustrating the concept:

```
function fn(arr):
    left = 0
    right = arr.length - 1

    while left < right:
        Do some logic here depending on the problem
        Do some more logic here to decide on one of the following:
            1. left++
            2. right--
            3. Both left++ and right--
```

The strength of this technique is that we will never have more than O(n) iterations of the while loop. This is because the pointers start n away from each other and move at least one step closer in every iteration. Therefore, if we can keep the work inside each iteration at O(1), this technique will result in a linear runtime, which is usually the best possible runtime. Let's look at some examples.

Example 1: Palindrome Check

```python
def check_if_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
```

Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise.

```python
def check_for_target(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        # curr is the current sum
        curr = nums[left] + nums[right]
        if curr == target:
            return True
        if curr > target:
            right -= 1
        else:
            left += 1

    return False
```

The reason this algorithm works: because the numbers are sorted, moving the left pointer permanently increases the value the left pointer points to (nums[left] = x). Similarly, moving the right pointer permanently decreases the value the right pointer points to (nums[right] = y). If we have x + y > target, then we can never have a solution with y because x can only increase. So if a solution exists, we can only find it by decreasing y. The same logic can be applied to x if x + y < target.

###  1.2. <a name='Movealongbothinputssimultaneouslyuntilallelementshavebeenchecked'></a>Move along both inputs simultaneously until all elements have been checked

Converting this idea into instructions:

1. Create two pointers, one for each iterable. Each pointer should start at the first index.
2. Use a while loop until one of the pointers reaches the end of its iterable.
3. At each iteration of the loop, move the pointers forward. This means incrementing either one of the pointers or both of the pointers. Deciding which pointers to move will depend on the problem we are trying to solve.
4. Because our while loop will stop when one of the pointers reaches the end, the other pointer will not be at the end of its respective iterable when the loop finishes. Sometimes, we need to iterate through all elements - if this is the case, you will need to write extra code here to make sure both iterables are exhausted.

Here's some pseudocode illustrating the concept:
```
function fn(arr1, arr2):
    i = j = 0
    while i < arr1.length AND j < arr2.length:
        Do some logic here depending on the problem
        Do some more logic here to decide on one of the following:
            1. i++
            2. j++
            3. Both i++ and j++

    // Step 4: make sure both iterables are exhausted
    // Note that only one of these loops would run
    while i < arr1.length:
        Do some logic here depending on the problem
        i++

    while j < arr2.length:
        Do some logic here depending on the problem
        j++
```

Similar to the first method we looked at, this method will have a linear time complexity of O(n+m) if the work inside the while loop is O(1), where n = arr1.length and m = arr2.length. This is because at every iteration, we move at least one pointer forward, and the pointers cannot be moved forward more than n + m times without the arrays being exhausted. Let's look at some examples.

Example 3: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.

```python
def combine(arr1, arr2):
    # ans is the answer
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    while j < len(arr2):
        ans.append(arr2[j])
        j += 1

    return ans
```

Like in the previous two examples, this algorithm has a time complexity of O(n) and uses O(1) space (if we don't count the output as extra space, which we usually don't).

Example 4: 392. Is Subsequence - Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

```python

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)

```

Just like all the prior examples, this solution uses O(1) space. The time complexity is linear with the lengths of s and t.

##  2. <a name='SlidingWindow'></a>Sliding Window

Like two pointers, sliding windows work the same with arrays and strings - the important thing is that they're iterables with ordered elements. A sliding window is actually implemented using two pointers!

###  2.1. <a name='Subarrays'></a>Subarrays

Given an array, a subarray is a contiguous section of the array. All the elements must be adjacent to each other in the original array and in their original order. For example, with the array [1, 2, 3, 4], the subarrays (grouped by length) are:

- Subarrays with length 1: [1], [2], [3], [4]
- Subarrays with length 2: [1, 2], [2, 3], [3, 4]
- Subarrays with length 3: [1, 2, 3], [2, 3, 4]
- Subarrays with length 4: [1, 2, 3, 4]

A subarray can be defined by two indices, the start and end. For example, with [1, 2, 3, 4], the subarray [2, 3] has a starting index of 1 and an ending index of 2. Let's call the starting index the left bound and the ending index the right bound. Another name for subarray in this context is "window".

A subarray is considered "valid" if it satisfies:
- a constraint metric.
- a numeric restriction on the constraint metric.

###  2.2. <a name='UsingSlidingWindow'></a>Using Sliding Window

Sliding window is used to analyze and find the valid subarrays of an array. The idea behind a sliding window is to maintain two variables, left and right. At any given time, left represents the left bound of our window, and right represents the right bound of our window.

Initially, we set left = right = 0, which means that the first window we consider is just the first element of the array on its own. We want to expand the size of our "window", and we do that by incrementing right. When we increment right, this is like "adding" a new element to our window. If by adding a new element the window becomes not-valid, we want to increment left until the window becomes valid again. Incrementing left is like "removing" an element from our window.

Whenever you see a problem that not only describes subarrays being "valid", but also asks you to find these subarrays, you should immediately think about sliding window.

###  2.3. <a name='ImplementationExamples'></a>Implementation Examples

Example 1: find the longest subarray with a sum less than or equal to k

```
function fn(nums, k):
    left = 0
    curr = 0
    answer = 0
    for (int right = 0; right < nums.length; right++):
        curr += nums[right]
        while (curr > k):
            curr -= nums[left]
            left++

        answer = max(answer, right - left + 1)

    return answer
```

or

```
function fn(arr):
    left = 0
    for (int right = 0; right < arr.length; right++):
        Do some logic to "add" element at arr[right] to window

        while WINDOW_IS_INVALID:
            Do some logic to "remove" element at arr[left] from window
            left++

        Do some logic to update the answer
```

Example 2: Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k. This is the problem we have been talking about above. We will now formally solve it.

```python
def find_length(nums, k):
    # curr is the current sum of the window
    left = curr = ans = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)

    return ans
```

Example 3: You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"? For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.

```python
def find_length(s):
    # curr is the current number of zeros in the window
    left = curr = ans = 0
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)

    return ans
```

Example 4: 713. Subarray Product Less Than K: Given an array of positive integers nums and an integer k, return the number of subarrays where the product of all the elements in the subarray is strictly less than k.

For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8. The subarrays with products less than k are:

[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

> The number of valid windows ending at index right is equal to the size of the window, which we know is right - left + 1.

```python
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        ans = left = 0
        curr = 1

        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1

            ans += right - left + 1

        return ans
```

Example 5: Fixed window size (pseudocode)

```
function fn(arr, k):
    curr = some data to track the window

    // build the first window
    for (int i = 0; i < k; i++)
        Do something with curr or other variables to build first window

    ans = answer variable, probably equal to curr here depending on the problem
    for (int i = k; i < arr.length; i++)
        Add arr[i] to window
        Remove arr[i - k] from window
        Update ans

    return ans
```

Example 6: Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.

```python
def find_best_subarray(nums, k):
    curr = 0
    for i in range(k):
        curr += nums[i]

    ans = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)

    return ans
```

# Prefix Sum

The idea is to create an array prefix where prefix[i] is the sum of all elements up to the index i (inclusive). For example, given nums = [5, 2, 1, 6, 3, 8], we would have prefix = [5, 7, 8, 14, 17, 25].

> When a subarray starts at index 0, it is considered a "prefix" of the array. A prefix sum represents the sum of all prefixes.

Prefix sums allow us to find the sum of any subarray in O(1). If we want the sum of the subarray from i to j (inclusive), then the answer is prefix[j] - prefix[i - 1], or alternatively prefix[j] - prefix[i] + nums[i] if you don't want to deal with the out of bounds case when i = 0.

Building a prefix sum is very simple. Here's some pseudocode:

```
Given an array nums,

prefix = [nums[0]]
for (int i = 1; i < nums.length; i++)
    prefix.append(nums[i] + prefix[prefix.length - 1])
```

A prefix sum is a great tool whenever a problem involves sums of a subarray. It only costs O(n) to build but allows all future subarray queries to be O(1), so it can usually improve an algorithm's time complexity by a factor of O(n), where n is the length of the array. Let's look at some examples.

Example 1: Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query. A query is true if the sum of the subarray from x to y is less than limit, or false otherwise. For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13, the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].

```python
def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    ans = []
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr < limit)

    return ans
```

With the prefix sum, it costs O(n) to build, but then answering each query is O(1). This gives a much better time complexity of O(n+m). We use O(n) space to build the prefix sum.

Example 2 - 2270: Number of ways to split array: Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a sum greater than or equal to the sum of the second section. The second section should have at least one number.

```python
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)

        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(nums[i] + prefix[-1])

        ans = 0
        for i in range(n - 1):
            left_section = prefix[i]
            right_section = prefix[-1] - prefix[i]
            if left_section >= right_section:
                ans += 1

        return ans
```

We can also do it without a prefix array:

```python
class Solution2:
    def waysToSplitArray(self, nums: list[int]) -> int:
        ans = left_section = 0
        total = sum(nums)

        for i in range(len(nums) - 1):
            left_section += nums[i]
            right_section = total - left_section
            if left_section >= right_section:
                ans += 1

        return ans
```