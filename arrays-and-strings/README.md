# Common Techniques and Patterns

<!-- vscode-markdown-toc -->
* 1. [Two Pointers](#TwoPointers)
	* 1.1. [Pointers at the Edges](#PointersattheEdges)
	* 1.2. [Move along both inputs simultaneously until all elements have been checked](#Movealongbothinputssimultaneouslyuntilallelementshavebeenchecked)

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

Example 4: 392. Is Subsequence.


