# Data Structures and Algorithms
A repository allowing me to track my study of data structures and algorithms.

## Installation

To install, first make sure you have `just` and `uv` installed. If you don't, run:

```bash
brew install just uv
```

Then, clone the repository and simply run:

```bash
just install
```

Finally, remember to install the pre-commit hooks:

```bash
pre-commit install
```

## Contents

The files are not intended to be ran as packages. Rather, they are the codes I wrote on platforms such as leetcode.com, hackerrank.com, etc. to solve various problems. Each file is named after the problem it solves. Also, each file contains a docstring at the top explaining the problem it solves, and the time/space complexity of the solution.

You can find me on LeetCode as [andreiroibu94](https://leetcode.com/u/andreiroibu94/).

## Big-O Notation Reference

### What Big-O actually measures

| Symbol         | Intuition                                                    | Common “shape”                                     |
| -------------- | ------------------------------------------------------------ | -------------------------------------------------- |
| **O(1)**       | *Constant*. Work doesn’t grow with input size.               | Array index, hash-table lookup, simple assignment. |
| **O(log n)**   | *Grows very slowly*. Each step roughly halves the problem.   | Binary search, tree height.                        |
| **O(n)**       | *Linear*. Double the input ⇒ \~double the work.              | Single loop over a list.                           |
| **O(n log n)** | *Linear-log*. A couple of “halve” operations inside a loop.  | Efficient sorts (merge sort, heap sort).           |
| **O(n²)**      | *Quadratic*. Work is proportional to “all pairs”.            | Two nested loops over the same n items.            |
| **O(2^n)**     | *Exponential*. Adds another doubling for each extra element. | Brute-force on every subset; quickly explodes.     |

### Time vs. Space

* **Time complexity**: how many basic operations an algorithm performs as input grows.
* **Space complexity**: how much *extra* memory it needs (beyond the input itself).

We drop constants and lower-order terms because they matter far less than the growth pattern when n becomes large.

### Reading a Big-O statement

Take “Running Sum: O(n) time, O(1) space”:

* If you hand it **2 ×** as many numbers, the running time should be roughly **2 ×** longer.
* Memory doesn’t budge (besides the input list itself).

### 3. Tips for thinking in Big-O

1. **Count loops** – each full loop over n elements suggests at least O(n). Nested loops multiply.
2. **Look for early exits** – `break` on a condition can make *average* time smaller, but worst-case Big-O usually stays the same.
3. **Ignore constants** – an algorithm that does 5n steps is still O(n).
4. **Space is separate** – in-place tricks often turn O(n) space into O(1) with the same time cost.