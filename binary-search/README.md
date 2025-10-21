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
```
The following template will find the right-most insertion point (the index of the right-most element plus one):

```python

def binary_search(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1

    return left
```

# 2. On Arrays

Binary search is a common optimization to a linear scan when searching for an element's index or insertion point if it doesn't exist. In these problems, left and right represent the bounds of the subarray we are currently considering. mid represents the index of the middle of the current search space. Sometimes, you will directly be binary searching for the answer. Other times, binary search will just be a tool that speeds up your algorithm.

## 2.1. Example 1 - Binary Search

You are given an array of integers nums which is sorted in ascending order, and an integer target. If target exists in nums, return its index. Otherwise, return -1.

