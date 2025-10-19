# Hashing

## 1.1. Introduction to Hash Maps

A hash function is a function that takes an input and deterministically converts it to an integer that is less than a fixed size set by the programmer. Inputs are called keys and the same input will always be converted to the same integer.

Because hash functions can convert any input into an integer, we can effectively remove the constraint of indices needing to be integers. When a hash function is combined with an array, it creates a hash map, also known as a hash table or dictionary.

With arrays, we map indices to values. With hash maps, we map keys to values, and a key can be almost anything. Typically, the only constraint on a hash map's key is that it has to be immutable (this is language dependent but generally a good rule of thumb). Values can be anything.

A hash map is probably the most important concept in all of algorithm interviewing. It is extremely powerful and allows you to reduce the time complexity of an algorithm by a factor of O(n) for a huge amount of problems.

To summarize, a hash map is an unordered data structure that stores key-value pairs. A hash map can add and remove elements in O(1), as well as update values associated with a key and check if a key exists, also in O(1). You can iterate over both the keys and values of a hash map, but the iteration won't necessarily follow any order.

The following operations are all O(1) for a hash map:

- Add an element and associate it with a value
- Delete an element if it exists
- Check if an element exists

The biggest disadvantage of hash maps is that for smaller input sizes, they can be slower due to overhead. Because big O ignores constants, the O(1) time complexity can sometimes be deceiving - it's usually something more like O(10). O(10) because every key needs to go through the hash function.

Hash tables can also take up more space. Dynamic arrays are actually fixed-size arrays that resize themselves when they go beyond their capacity. Hash tables are also implemented using a fixed size array - remember that the size is a limit set by the programmer. The problem is, resizing a hash table is much more expensive because every existing key needs to be re-hashed, and also a hash table may use an array that is significantly larger than the number of elements stored, resulting in a huge waste of space. When you don't know how many elements you need to store, arrays are more flexible with resizing and not wasting space.

>  The constant time operations are only constant relative to the size of the map.

## 1.2. Introduction to Sets

A set is another data structure that is very similar to a hash table. It uses the same mechanism for hashing keys into integers. The difference between a set and hash table is that sets do not map their keys to anything. Sets are more convenient to use when you only care about checking if elements exist. You can add, remove, and check if an element exists in a set all in O(1).

An important thing to note about sets is that they don't track frequency. If you have a set and add the same element 100 times, the first operation adds it and the next 99 do nothing.

> A set is basically a hash map if you only consider the keys.

## 1.3. Interface Guide

```python
# Declaration: a hash map is declared like any other variable. The syntax is {}
hash_map = {}

# If you want to initialize it with some key value pairs, use the following syntax:
hash_map = {1: 2, 5: 3, 7: 2}

# Checking if a key exists: simply use the `in` keyword
1 in hash_map # True
9 in hash_map # False

# Accessing a value given a key: use square brackets, similar to an array.
hash_map[5] # 3

# Adding or updating a key: use square brackets, similar to an array.
# If the key already exists, the value will be updated
hash_map[5] = 6

# If the key doesn't exist yet, the key value pair will be inserted
hash_map[9] = 15

# Deleting a key: use the del keyword. Key must exist or you will get an error.
del hash_map[9]

# Get size
len(hash_map) # 3

# Get keys: use .keys(). You can iterate over this using a for loop.
keys = hash_map.keys()
for key in keys:
    print(key)

# Get values: use .values(). You can iterate over this using a for loop.
values = hash_map.values()
for val in values:
    print(val)

# Get key value pairs: use .items(). You can iterate over this using a for loop.
items = hash_map.items()
for key, val in items:
    print(key, val)
```

# 2. Checking for Existence

One of the most common applications of a hash map or set is determining if an element exists in O(1). Since an array needs O(n) to do this, using a hash map or set can improve the time complexity of an algorithm greatly, usually from O(n^2) to O(n).

## 2.1. Example 1 - Two Sum

Given an array of integers nums and an integer target, return indices of two numbers such that they add up to target. You cannot use the same index twice.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in dic: # This operation is O(1)!
                return [i, dic[complement]]

            dic[num] = i

        return [-1, -1]
```

If the question wanted us to return a boolean indicating if a pair exists or to return the numbers themselves, then we could just use a set. However, since it wants the indices of the numbers, we need to use a hash map to "remember" what indices the numbers are at.

## 2.2. Example 2 - First Letter to Appear Twice

Given a string s, return the first character to appear twice. It is guaranteed that the input will have a duplicate character.

```python
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for c in s:
            if c in seen:
                return c
            seen.add(c)

        return " "
```

Here, our time complexity is O(n) because we only need to iterate through the string once, and each existence check and insertion into the set is O(1). The space complexity can be either O(1) or O(n) depending on how you look at it. Since there are only 26 lowercase English letters, the maximum size of the set is 26, which is a constant. However, if you consider the input size n to be variable and unbounded, then in the worst case (if the input was not guaranteed to have duplicates), we could have to store all n characters in the set, resulting in O(n) space complexity.

## 2.3. Example 3 - Find Numbers with No Adjacent Elements

Given an integer array nums, find all the numbers x in nums that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.

If a valid number x appears multiple times, you only need to include it in the answer once.

```python
def find_numbers(nums):
    ans = []
    nums_set = set(nums)

    for num in nums_set:
        if (num + 1 not in nums_set) and (num - 1 not in nums_set):
            ans.append(num)

    return ans
```

Because the checks are O(1), the time complexity is O(n) since each for loop iteration runs in constant time. The set will occupy O(n) space.

# 3. Counting

Counting is a very common pattern with hash maps. By "counting", we are referring to tracking the frequency of things. This means our hash map will be mapping keys to integers. Anytime you need to count anything, think about using a hash map to do it.

## 3.1. Example 1 - Counting Elements

Example 1: You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.

For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".

> In Python, the collections module provides very useful data structures. We will be using a defaultdict in the Python code. Functionality-wise, a defaultdict is the same as a hash map, it's just more pleasant to work with.

```python

from collections import defaultdict

def find_longest_substring(s, k):
    counts = defaultdict(int)
    left = ans = 0
    for right in range(len(s)):
        counts[s[right]] += 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1

        ans = max(ans, right - left + 1)

    return ans

```

As you can see, using a hash map to store the frequency of any key we want allows us to solve sliding window problems that put constraints on multiple elements. We know from earlier that the time complexity of sliding window problems are O(n) if the work done inside each for loop iteration is amortized constant, which is the case here due to a hash map having O(1) operations. The hash map occupies O(k) space, as the algorithm will delete elements from the hash map once it grows beyond k.

## 3.2. Example 2 - Intersection of Multiple Arrays

Given a 2D array nums that contains n arrays of distinct integers, return a sorted array containing all the numbers that appear in all n arrays.

For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4]. 3 and 4 are the only numbers that are in all arrays.

```python
from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)
        for arr in nums:
            for x in arr:
                counts[x] += 1

        n = len(nums)
        ans = []
        for key in counts:
            if counts[key] == n:
                ans.append(key)

        return sorted(ans)
```

Let's say that there are n lists and each list has an average of m elements. To populate our hash map, it costs O(n⋅m) to iterate over all the elements. The next loop iterates over all unique elements that we encountered. If all elements are unique, this can cost up to O(n⋅m), although this won't affect our time complexity since the previous loop also cost O(n⋅m). Finally, there can be at most m elements inside ans when we perform the sort, which means in the worst case, the sort will cost O(m⋅logm). This gives us a time complexity of O(n⋅m+m⋅logm)=O(m⋅(n+logm)). If every element in the input is unique, then the hash map will grow to a size of n⋅m, which means the algorithm has a space complexity of O(n⋅m).

## 3.3. Example 3 - Check if All Characters Have Equal Number of Occurrences

Given a string s, determine if all characters have the same frequency.

For example, given s = "abacbc", return true, because all characters appear twice. Given s = "aaabb", return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.

```python
from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1

        frequencies = counts.values()
        return len(set(frequencies)) == 1
```

Given n as the length of s, it costs O(n) to populate the hash map, then O(n) to convert the hash map's values to a set. This gives us a time complexity of O(n). The space that the hash map and set would occupy is equal to the number of unique characters. As previously discussed, some people would argue that this is O(1) since the characters come from the English alphabet, which is bounded by a constant. A more general answer would be to say that the space complexity is O(k), where k is the number of characters that could be in the input, which happens to be 26 in this problem.

> ALTERNATIVE SOLUTION

```python
from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1
```

## 3.4. Example 4 - Subarray Sum Equals K // Count the number of subarrays with an "exact" constraint

Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.

```python
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for num in nums:
            curr += num
            ans += counts[curr - k]
            counts[curr] += 1

        return ans
```

The time and space complexity of this algorithm are both O(n), where n is the length of nums. Each for loop iteration runs in constant time and the hash map can grow to a size of n elements.

## 3.5. Example 5 - Count Number of Nice Subarrays

Given an array of positive integers nums and an integer k. Find the number of subarrays with exactly k odd numbers in them.

For example, given nums = [1, 1, 2, 1, 1], k = 3, the answer is 2. The subarrays with 3 odd numbers in them are [1, 1, 2, 1, 1] and [1, 1, 2, 1, 1].

```python
from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for num in nums:
            curr += num % 2
            ans += counts[curr - k]
            counts[curr] += 1

        return ans
```

The time and space complexity of this algorithm is identical to the previous problem's (O(n) for both) for the same reasons. Remember when we said, "you'll see how similar the code is for each problem that falls in this pattern"? Two different problems and the difference in the code is literally 2 characters, "% 2". Note that while not all problems that follow this pattern will use identical code, they will all still be very similar.