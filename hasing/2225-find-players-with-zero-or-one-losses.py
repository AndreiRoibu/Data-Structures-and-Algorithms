# You are given an integer array matches where matches[i] = [winneri, loseri]
# indicates that the player winneri defeated player loseri in a match.

# Return a list answer of size 2 where:

# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.

# Note:

# You should only consider the players that have played at least one match.
# The testcases will be generated such that no two matches will have the same
# outcome.


# Example 1:

# Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],
#                   [10,9]]
# Output: [[1,2,10],[4,5,7,8]]
# Explanation:
# Players 1, 2, and 10 have not lost any matches.
# Players 4, 5, 7, and 8 each have lost one match.
# Players 3, 6, and 9 each have lost two matches.
# Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
# Example 2:

# Input: matches = [[2,3],[1,3],[5,4],[6,4]]
# Output: [[1,2,5,6],[]]
# Explanation:
# Players 1, 2, 5, and 6 have not lost any matches.
# Players 3 and 4 each have lost two matches.
# Thus, answer[0] = [1,2,5,6] and answer[1] = [].


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        losses_count = {}

        for winner, loser in matches:
            losses_count[winner] = losses_count.get(winner, 0)
            losses_count[loser] = losses_count.get(loser, 0) + 1

        won_all, lost_one = [], []
        for player, count in losses_count.items():
            if count == 0:
                won_all.append(player)
            if count == 1:
                lost_one.append(player)

        return [sorted(won_all), sorted(lost_one)]


# Complexity Analysis
# Time Complexity: O(N log N), where N is the number of unique players. For each
# match, we perform O(1) operations to update the loss count in the dictionary.
# After processing all matches, we sort the lists of players who have won all,
# which is O(N log N) in the worst case.
# Space Complexity: O(N), where N is the number of unique players. We use a
# dictionary to store the loss counts for each player.
