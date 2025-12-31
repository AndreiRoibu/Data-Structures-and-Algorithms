# You are given two positive integer arrays spells and potions, of length n and
# m respectively, where spells[i] represents the strength of the ith spell
# and potions[j] represents the strength of the jth potion.

# You are also given an integer success. A spell and potion pair is considered
#  successful if the product of their strengths is at least success.

# Return an integer array pairs of length n where pairs[i] is the number of
# potions that will form a successful pair with the ith spell.


# Example 1:

# Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
# Output: [4,0,3]
# Explanation:
# - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
# - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
# - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
# Thus, [4,0,3] is returned.
# Example 2:

# Input: spells = [3,1,2], potions = [8,5,8], success = 16
# Output: [2,0,2]
# Explanation:
# - 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
# - 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful.
# - 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful.
# Thus, [2,0,2] is returned.


# Constraints:

# n == spells.length
# m == potions.length
# 1 <= n, m <= 105
# 1 <= spells[i], potions[i] <= 105
# 1 <= success <= 1010


# Hint 1
# Notice that if a spell and potion pair is successful, then the spell and
# all stronger potions will be successful too.

# Hint 2
# Thus, for each spell, we need to find the potion with the least strength
# that will form a successful pair.

# Hint 3
# We can efficiently do this by sorting the potions based on strength and
# using binary search.


class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        answer = []
        m = len(potions)

        def binary_search_leftmost(arr, target):
            left = 0
            right = len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left

        for spell in spells:
            idx = binary_search_leftmost(arr=potions, target=success / spell)
            answer.append(m - idx)

        return answer


# Explanation:
# - Sort potions so stronger potions appear to the right.
# - For each spell, binary search the first potion that reaches success / spell.
# - All potions from that index to the end form successful pairs.
# - We use a subset of binary search to find the leftmost index where potions[i] >= target.
# - We use the leftmost index because all potions to the right will also satisfy the condition.

# Complexity Analysis:
# Time Complexity: O((m + n) log m), where n is the length of spells and m is the
# length of potions. We sort the potions array in O(m log m) time, and for each spell,
# we perform a binary search on the potions array which takes O(log m) time. Thus, the overall time complexity is
# O(m log m + n log m) = O((m + n) log m).
# Space Complexity: O(1), as we are using only a constant amount of extra
# space.
