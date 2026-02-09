# You are given the array paths, where paths[i] = [cityAi, cityBi] means there
# exists a direct path going from cityAi to cityBi. Return the destination city,
#  that is, the city without any path outgoing to another city.

# It is guaranteed that the graph of paths forms a line without any loop,
# therefore, there will be exactly one destination city.


# Example 1:

# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo"
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which
# is the destination city. Your trip consist of: "London" -> "New York" ->
# "Lima" -> "Sao Paulo".
# Example 2:

# Input: paths = [["B","C"],["D","B"],["C","A"]]
# Output: "A"
# Explanation: All possible trips are:
# "D" -> "B" -> "C" -> "A".
# "B" -> "C" -> "A".
# "C" -> "A".
# "A".
# Clearly the destination city is "A".
# Example 3:

# Input: paths = [["A","Z"]]
# Output: "Z"


# Constraints:

# 1 <= paths.length <= 100
# paths[i].length == 2
# 1 <= cityAi.length, cityBi.length <= 10
# cityAi != cityBi
# All strings consist of lowercase and uppercase English letters and the space character.

# Hint 1
# Start in any city and use the path to move to the next city.
# Hint 2
# Eventually, you will reach a city with no path outgoing, this is the destination city.


class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        sources = set()
        destinations = set()
        for path in paths:
            sources.add(path[0])
            destinations.add(path[1])

        return destinations.difference(sources).pop()


# ### Summary Explainer (Future Reference)
# - **Identify Start vs. End**: You iterate through all paths, separating
# starting cities (`sources`) from destination cities (`destinations`).
# - **Set Operations**: You store all sources and destinations in two separate
# sets.
# - **Find the Leaf Node**: Since the destination city never acts as a starting
# point, you find the difference `destinations - sources`.
# - **Return Result**: The single remaining city in the difference set is the
# final destination.

# ### Complexity Analysis
# - **Time Complexity: O(N)**
#   - Let $N$ be the number of paths (which corresponds to the number of edges).
#   - Iterating through the list takes $O(N)$.
#   - Adding to a set takes $O(1)$ on average.
#   - The set difference operation takes $O(N)$ in the worst case (iterating over the sets).
#   - Overall, the process is linear with respect to the input size.

# - **Space Complexity: O(N)**
#   - You store all cities in two sets (`sources` and `destinations`).
#   - In the worst case, there are $N$ paths and up to $2N$ distinct cities
# (though practically $N+1$ cities in a linear path), so space usage is linear.


class Solution2:
    def destCity(self, paths: list[list[str]]) -> str:
        sources = set()
        for path in paths:
            sources.add(path[0])

        for path in paths:
            if path[1] not in sources:
                return path[1]


# Minor Space Optimization: We don't actually need to store the destinations in
# a set. We can just put all sources in a set. Then iterate through the list of
# paths again; if a destination path[1] is not in the sources set, that's your answer.
# This saves the space overhead of the second set, though it remains O(N) overall.
