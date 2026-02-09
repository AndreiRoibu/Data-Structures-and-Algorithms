# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing
# moving one unit north, south, east, or west, respectively. You start at the
# origin (0, 0) on a 2D plane and walk on the path specified by path.

# Return true if the path crosses itself at any point, that is, if at any time
#  you are on a location you have previously visited. Return false otherwise.


# Example 1:


# Input: path = "NES"
# Output: false
# Explanation: Notice that the path doesn't cross any point more than once.
# Example 2:


# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.


# Constraints:

# 1 <= path.length <= 104
# path[i] is either 'N', 'S', 'E', or 'W'.

# Hint 1
# Simulate the process while keeping track of visited points.

# Hint 2
# Use a set to store previously visited points.


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        directions = {"N": (0, 1), "S": (0, -1), "E": (-1, 0), "W": (1, 0)}
        visited = {(x, y)}
        for char in path:
            dx, dy = directions[char]
            x += dx
            y += dy
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False


# ### Summary Explainer (Future Reference)
# - **Track Coordinates**: Uses variables `x` and `y` starting at `(0, 0)` to
#   simulate movement on a 2D plane.
# - **Direction Mapping**: Uses a dictionary to map 'N', 'S', 'E', 'W' characters
#   to their respective changes in x and y coordinates.
# - **Hash Set for History**: Stores every visited coordinate tuple `(x, y)` in a
#   set called `visited`.
# - **Duplicate Check**: Before adding a new coordinate to the set, it checks if
#  `(x, y)` is already present. If it is, the path has crossed itself, so it
#   returns `True`.

# ### Complexity Analysis
# - **Time Complexity: O(N)**
#   - $N$ is the length of the string `path`.
#   - The code iterates through each character exactly once.
#   - Dictionary lookups, coordinate updates, set checks (`in`), and set insertions
#       (`add`) are all **O(1)** operations on average.
#   - Thus, the total time is linear.
# - **Space Complexity: O(N)**
#   - In the worst case (no crossing), the path visits $N + 1$ unique coordinates.
#   - Storing all these unique tuples in the `visited` set requires **O(N)** space.
