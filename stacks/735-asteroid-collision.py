# We are given an array asteroids of integers representing asteroids in a row.
# The indices of the asteroid in the array represent their relative position in
# space.

# For each asteroid, the absolute value represents its size, and the sign
# represents its direction (positive meaning right, negative meaning left).
# Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids
# meet, the smaller one will explode. If both are the same size, both will explode.
# Two asteroids moving in the same direction will never meet.


# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# Example 2:

# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# Example 3:

# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide
# resulting in 10.
# Example 4:

# Input: asteroids = [3,5,-6,2,-1,4]​​​​​​​
# Output: [-6,2,4]
# Explanation: The asteroid -6 makes the asteroid 3 and 5 explode, and then
# continues going left. On the other side, the asteroid 2 makes the asteroid -1
# explode and then continues going right, without reaching asteroid 4.

# Hint 1
# Say a row of asteroids is stable. What happens when a new asteroid is added on
# the right?


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        """
        Resolves collisions between a sequence of asteroids.

        Asteroids are represented by integers where the absolute value denotes size,
        and the sign denotes direction (positive = right, negative = left).
        Asteroids moving in the same direction or moving away from each other
        will never collide. When two asteroids collide, the smaller one is
        destroyed. If they are the same size, both are destroyed.

        Args:
            asteroids (List[int]): A list of integers representing the asteroids.

        Returns:
            List[int]: The state of the asteroids after all collisions are resolved.

        Time Complexity:
            O(N): Where N is the number of asteroids. We iterate through the list
            once. In the worst case, an asteroid might cause multiple pops from
            the stack, but every asteroid is pushed to the stack at most once
            and popped from the stack at most once. Thus, the amortized work
            per asteroid is O(1).

        Space Complexity:
            O(N): In the worst-case scenario (e.g., all asteroids moving in the
            same direction or moving away from each other like `[-5, -5, 5, 5]`),
            no collisions occur, and all N asteroids will be stored in the stack.
        """
        # The stack `ans` will hold the surviving asteroids.
        ans = []

        # Iterate through each asteroid in the given list
        for elem in asteroids:
            # We start by assuming the current asteroid will survive any potential collisions.
            survived = True

            # A collision ONLY happens when the asteroid at the top of the stack
            # is moving Right (ans[-1] > 0) AND the new asteroid is moving Left (elem < 0).
            while ans and ans[-1] > 0 and elem < 0:
                # Scenario 1: The stack asteroid is smaller than the new asteroid.
                if ans[-1] < abs(elem):
                    # The stack asteroid is destroyed.
                    ans.pop()
                    # The new asteroid (`elem`) continues moving left.
                    # We use `continue` to jump back to the start of the `while`
                    # loop to check if `elem` collides with the NEXT asteroid in the stack.
                    continue

                # Scenario 2: The stack asteroid and the new asteroid are the exact same size.
                elif ans[-1] == abs(elem):
                    # Mutual destruction: Both asteroids are destroyed.
                    # Pop the stack asteroid...
                    ans.pop()
                    # ...and mark the new asteroid as destroyed so we don't append it later.
                    survived = False
                    # The new asteroid is gone, so no more collisions can happen. Break the loop.
                    break

                # Scenario 3: The stack asteroid is strictly larger than the new asteroid.
                else:
                    # The new asteroid (`elem`) is destroyed.
                    survived = False
                    # Since `elem` is destroyed, it can't collide with anything else. Break the loop.
                    break

            # If the new asteroid survived all collisions (or if no collisions happened),
            # safely add it to the stack of survivors.
            if survived:
                ans.append(elem)

        return ans
