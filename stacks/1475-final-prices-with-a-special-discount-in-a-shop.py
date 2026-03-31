# You are given an integer array prices where prices[i] is the price of the ith
# item in a shop.

# There is a special discount for items in the shop. If you buy the ith item,
# then you will receive a discount equivalent to prices[j] where j is the
# minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will
# not receive any discount at all.

# Return an integer array answer where answer[i] is the final price you will
# pay for the ith item of the shop, considering the special discount.


# Example 1:

# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]
# Explanation:
# For item 0 with price[0]=8 you will receive a discount equivalent to
# prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
# For item 1 with price[1]=4 you will receive a discount equivalent to
# prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
# For item 2 with price[2]=6 you will receive a discount equivalent to
# prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
# For items 3 and 4 you will not receive any discount at all.
# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: [1,2,3,4,5]
# Explanation: In this case, for all items, you will not receive any discount at
# all.
# Example 3:

# Input: prices = [10,1,1,6]
# Output: [9,0,1,6]


# Constraints:

# 1 <= prices.length <= 500
# 1 <= prices[i] <= 1000

# Hint 1
# Use brute force: For the ith item in the shop with a loop find the first
# position j satisfying the conditions and apply the discount, otherwise, the
# discount is 0.


class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        """
        Calculates the final prices of items after applying a special discount.

        This solution uses a monotonic stack to efficiently find the next smaller or
        equal price for each item. The stack keeps track of the indices of the
        items for which we haven't found a discount yet. When we encounter a
        price that is less than or equal to the price at the top of the stack,
        we apply the discount.

        Args:
            prices (List[int]): A list where prices[i] is the price of the ith item in a shop.

        Returns:
            List[int]: A list of final prices after all possible discounts are applied.

        Time Complexity:
            O(N): Where N is the number of items. Each index is pushed onto and popped from the stack at most once, making the while loop run O(N) times overall.

        Space Complexity:
            O(N): In the worst-case scenario (e.g., strictly increasing prices), the stack can grow up to size N.
        """
        stack = []

        # We maintain a monotonically increasing stack.
        # The stack keeps track of the indices, but we compare the actual prices!
        for i, price in enumerate(prices):
            # While the stack is not empty and the current price is less than
            # or equal to the price of the item at the index stored at the top of the stack:
            while stack and prices[stack[-1]] >= price:
                # Pop the index of the item that will receive the current price as a discount
                j = stack.pop()

                # Apply the discount to the original price in-place
                prices[j] = prices[j] - price

            # Add the current index to the stack to potentially find a discount for it later
            stack.append(i)

        # Return the modified array containing the final prices
        return prices
