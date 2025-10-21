# Binary Search

## 1.1 Introduction to Binary Search

Binary search is a search algorithm that runs in O(log n) in the worst case, where n is the size of the search space. For binary search to work, your search space usually needs to be sorted. Binary search trees, which we looked at in the trees and graphs chapter, are based on binary search.

If you have a sorted array arr and an element x, then in O(log n) time and O(1) space, binary search can:
- Find the index of x if it is in arr
- Find the first or the last index in which x can be inserted to maintain being sorted otherwise

Here's the idea behind binary search:

Let's say that there is a sorted integer array arr, and you know that the number x is in it, but you don't know at what index. You want to find the position of x. Start by checking the element in the middle of arr. If this element is too small, then we know every element in the left half will also be too small, since the array is sorted. Similarly, if the element is too large, then every element in the right half will also be too large.

We can discard the half that can't contain x, and then repeat the process on the other half. We continue this process of cutting the array in half until we find x.

This is how binary search is implemented:

1. Declare left = 0 and right = arr.length - 1. These variables represent the inclusive bounds of the current search space at any given time. Initially, we consider the entire array.
2. While left <= right:
   1. Calculate the middle of the current search space, mid = (left + right) // 2 (floor division)
   2. Check arr[mid]. There are 3 possibilities:
      1. If arr[mid] = x, then the element has been found, return.
      2. If arr[mid] > x, then halve the search space by doing right = mid - 1.
      3. If arr[mid] < x, then halve the search space by doing left = mid + 1.
3. If you get to this point without arr[mid] = x, then the search was unsuccessful. The left pointer will be at the index where x would need to be inserted to maintain arr being sorted.

Because the search space is halved at every iteration, binary search's worst-case time complexity is O(log n). This makes it an extremely powerful algorithm as logarithmic time is very fast compared to linear time.

You should think about binary search anytime the problem provides anything sorted. O(log n) is extremely fast and binary search is usually a huge optimization.

## 1.2. Implementation Template

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            # do something
            return
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    # target is not in arr, but left is at the insertion point
    return left
```

## 1.3. Duplicate Elements

If your input has duplicates, you can modify the binary search template to find either the first or the last position of a given element. If target appears multiple times, then the following template will find the left-most index:

```python
def binary_search_leftmost(arr, target):
    left = 0
    right = len(arr)                # DIFF vs. Std
    while left < right:             # DIFF vs. Std
        mid = (left + right) // 2
        if arr[mid] >= target:      # DIFF vs. Std
            right = mid             # DIFF vs. Std
        else:
            left = mid + 1

    return left
```
The following template will find the right-most insertion point (the index of the right-most element plus one):

```python

def binary_search_rightmost(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:   # DIFF vs. Leftmost
            right = mid
        else:
            left = mid + 1

    return left
```

# 2. On Arrays

Binary search is a common optimization to a linear scan when searching for an element's index or insertion point if it doesn't exist. In these problems, left and right represent the bounds of the subarray we are currently considering. mid represents the index of the middle of the current search space. Sometimes, you will directly be binary searching for the answer. Other times, binary search will just be a tool that speeds up your algorithm.

## 2.1. Example 1 - Binary Search

You are given an array of integers nums which is sorted in ascending order, and an integer target. If target exists in nums, return its index. Otherwise, return -1.

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            num = nums[mid]

            if num == target:
                return mid

            if num > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
```

## 2.2. Example 2 - Search a 2D Matrix

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. Integers in each row are sorted from left to right. The first integer of each row is greater than the last integer of the previous row.

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            num = matrix[row][col]

            if num == target:
                return True

            if num < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
```

Because there are O(m⋅n) elements, the initial search space has a size of O(m⋅n), which means this algorithm has a time complexity of O(log(m⋅n)). We don't use any extra space except for a few integer variables.

## Example 3 - Successful Pairs of Spells and Potions

You are given two positive integer arrays spells and potions, where spells[i] represents the strength of the i-th spell and potions[j] represents the strength of the j-th potion. You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success. For each spell, find how many potions it can pair with to be successful. Return an integer array where the i-th element is the answer for the i-th spell.

```python
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binary_search(arr, target):
            left = 0
            right = len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] >= target:
                    right = mid
                else:
                    left = mid + 1

            return left

        potions.sort()
        ans = []
        m = len(potions)

        for spell in spells:
            i = binary_search(potions, success / spell)
            ans.append(m - i)

        return ans

```

To sort potions, it costs O(m⋅logm). Then, we iterate n times, performing a O(logm) binary search on each iteration. This gives us a time complexity of O((m+n)⋅logm), which is much faster than O(m⋅n) because logm is small. Because we are sorting the input, some space is used depending on the sorting algorithm used by your language.

Binary searching on an array is a simple tool to improve an algorithm's time complexity by a huge amount. Anytime you have a sorted array (or are able to sort an array without consequence), consider using binary search to quickly find the insertion index of a desired element. Try these upcoming practice problems before moving on to the next pattern.