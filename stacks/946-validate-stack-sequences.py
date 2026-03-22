# Given two integer arrays pushed and popped each with distinct values, return
# true if this could have been the result of a sequence of push and pop
# operations on an initially empty stack, or false otherwise.


# Example 1:

# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4),
# pop() -> 4,
# push(5),
# pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
# Example 2:

# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.


# Constraints:

# 1 <= pushed.length <= 1000
# 0 <= pushed[i] <= 1000
# All the elements of pushed are unique.
# popped.length == pushed.length
# popped is a permutation of pushed.


class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        """
        Validates whether the given pushed and popped sequences could represent
        the result of a sequence of push and pop operations on an initially empty stack.

        Explainer:
        We simulate the push and pop operations using an actual stack (`stack_pushed`).
        For each element in the `pushed` array, we push it onto our simulated stack.
        Then, we greedily pop elements from the simulated stack as long as the top
        element matches the current expected element in the `popped` array.
        If the sequences are valid, we will be able to successfully process and pop
        all elements, meaning our `idx_popped` pointer will reach the end of `popped`.

        Args:
            pushed (List[int]): An array of distinct integers representing elements pushed.
            popped (List[int]): An array of distinct integers representing elements popped.

        Returns:
            bool: True if the sequences are a valid push/pop combination, False otherwise.

        Time Complexity:
            O(N): Where N is the length of `pushed`. We iterate through `pushed` once,
                  and each element is pushed to and popped from `stack_pushed` at most once.
        Space Complexity:
            O(N): Where N is the length of `pushed`. In the worst case (e.g., all pushes
                  happen before any pops), `stack_pushed` will store all N elements.
        """
        # Pointer to track the current element we want to pop from the 'popped' sequence
        idx_popped = 0

        # Cache the length of the popped array for bounds checking
        len_popped = len(popped)

        # Simulated stack to keep track of the elements being pushed
        stack_pushed = []

        # Process each element in the pushed sequence
        for element in pushed:
            # Simulate the push operation
            stack_pushed.append(element)

            # Greedily pop while the top of our stack matches the expected popped element
            # Condition 1: stack_pushed is not empty (prevents IndexError)
            # Condition 2: idx_popped is within bounds of the popped array
            # Condition 3: The top of stack_pushed matches the current required popped element
            while stack_pushed and idx_popped < len_popped and stack_pushed[-1] == popped[idx_popped]:
                stack_pushed.pop()  # Perform the pop operation
                idx_popped += 1  # Advance our pointer to the next expected popped element

        # If we successfully verified all pops, our pointer will have reached the length of popped
        return idx_popped == len_popped


# ------------------------------------------------------------------------------
# O(1) space solution using the input array as a stack
# ------------------------------------------------------------------------------
# Instead of creating a new list, we use a two-pointer approach where we treat
# the beginning of the pushed array as our stack. We overwrite values in pushed
# as we go, using a pointer i to keep track of the "top" of our in-place stack.
#
# In professional environments, mutating input variables to save space isn't
# always recommended if the original data needs to be preserved. Our current
# O(N) space implementation is safer and heavily preferred in most real-world
# scenarios.


class Solution2:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        # 'i' represents the top of our in-place stack.
        # It also serves as the index where the next element should be placed.
        i = 0

        # 'j' is the pointer for the 'popped' sequence.
        j = 0

        for x in pushed:
            # "Push" the current element onto our in-place stack
            pushed[i] = x

            # Greedily "pop" if the top of our stack matches the expected popped element
            # i >= 0 ensures the stack is not empty
            while i >= 0 and pushed[i] == popped[j]:
                i -= 1  # Move the stack top pointer down (simulating a pop)
                j += 1  # Move to the next expected popped element

            # Move the pointer up to prepare for the next element to be pushed
            i += 1

        # If the stack is empty at the end, 'i' will have been reduced to 0
        return i == 0


# How this works:

# 1. i (Stack Pointer): As we iterate through the pushed array, we place the
#   current element x at pushed[i]. At this moment, i is the index of the top
#   of the stack.
# 2. The while loop: We check if the element at our current stack top
#   (pushed[i]) equals the currently required element from popped (popped[j]).
# 3. Simulating Pops (i -= 1): If they match, we decrement i to "pop" the element,
#   essentially forgetting about it. We also increment j to look for the next
#   required pop.
# 4. Preparing the next push (i += 1): Once we are done popping, we increment i
#   so the next number in the for loop gets written to the correct position
#   (overwriting elements we've already "popped").

# Complexity:

# Time Complexity: O(N) - We still process each element exactly once (it is
# written once and decremented/popped at most once).
# Space Complexity: O(1) - We only use two integer pointers (i and j) and reuse
# the input array, allocating no extra space. (Note: Mutating inputs is a
# great trick for coding interviews to show optimization skills, though in a
# real production environment, you might prefer your original O(N) space
# solution to avoid altering the incoming data).
