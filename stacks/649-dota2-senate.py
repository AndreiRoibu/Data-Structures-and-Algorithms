# In the world of Dota2, there are two parties: the Radiant and the Dire.

# The Dota2 senate consists of senators coming from two parties. Now the Senate
# wants to decide on a change in the Dota2 game. The voting for this change is a
#  round-based procedure. In each round, each senator can exercise one of the
# two rights:

# Ban one senator's right: A senator can make another senator lose all his
# rights in this and all the following rounds.
# Announce the victory: If this senator found the senators who still have rights
# to vote are all from the same party, he can announce the victory and decide on
# the change in the game.
# Given a string senate representing each senator's party belonging. The
# character 'R' and 'D' represent the Radiant party and the Dire party. Then if
# there are n senators, the size of the given string will be n.

# The round-based procedure starts from the first senator to the last senator in
# the given order. This procedure will last until the end of voting. All the
# senators who have lost their rights will be skipped during the procedure.

# Suppose every senator is smart enough and will play the best strategy for his
# own party. Predict which party will finally announce the victory and change
# the Dota2 game. The output should be "Radiant" or "Dire".


# Example 1:

# Input: senate = "RD"
# Output: "Radiant"
# Explanation:
# The first senator comes from Radiant and he can just ban the next senator's
# right in round 1.
# And the second senator can't exercise any rights anymore since his right has
# been banned.
# And in round 2, the first senator can just announce the victory since he is
# the only guy in the senate who can vote.
# Example 2:

# Input: senate = "RDD"
# Output: "Dire"
# Explanation:
# The first senator comes from Radiant and he can just ban the next senator's
# right in round 1.
# And the second senator can't exercise any rights anymore since his right has
# been banned.
# And the third senator comes from Dire and he can ban the first senator's
# right in round 1.
# And in round 2, the third senator can just announce the victory since he is
# the only guy in the senate who can vote.


# Constraints:

# n == senate.length
# 1 <= n <= 104
# senate[i] is either 'R' or 'D'.

from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """
        Predicts which party will declare victory in the Dota2 Senate.

        This approach uses a queue to simulate the round-based voting process.
        Each senator greedily bans the next available senator from the opposing
        party. Instead of searching for the next opponent, we keep track of
        pending bans (`r_banned` and `d_banned`). When a senator's turn comes,
        if there's a pending ban against their party, they are removed.
        Otherwise, they issue a ban against the opposing party and rejoin the
        queue for the next round.

        Args:
            senate (str): A string representing the initial sequence of senators,
                where 'R' stands for Radiant and 'D' stands for Dire.

        Returns:
            str: The name of the winning party, either 'Radiant' or 'Dire'.

        Time Complexity:
            O(N): Where N is the length of the senate string. Each round
            eliminates a fraction of the remaining senators. The total queue
            operations sum to a geometric series (N + N/2 + N/4 + ...), which
            bounds the overall time complexity to O(N).

        Space Complexity:
            O(N): We use a deque to store the active senators, taking
            up to O(N) extra space.
        """
        # Calculate the total number of eligible senators for each party initially.
        r_count = senate.count("R")
        d_count = len(senate) - r_count

        # Ban trackers ("floating bans") to keep count of how many senators
        # from each party are slated to be banned but haven't been popped yet.
        r_banned = 0
        d_banned = 0

        # Initialize the queue with the initial order of the senate.
        queue = deque(senate)

        # Process the queue as long as both parties still have eligible senators.
        # Once one party reaches 0 count, the other party wins.
        while r_count and d_count:
            # Get the senator whose turn it is to vote.
            current_senator = queue.popleft()

            # Process Dire senator
            if current_senator == "D":
                if d_banned:
                    # There is a pending ban against Dire. This senator is eliminated.
                    d_banned -= 1
                    d_count -= 1
                else:
                    # No pending ban against Dire. This senator is eligible to vote.
                    # Greedily issue a ban against the next available Radiant senator.
                    r_banned += 1
                    # After voting, the senator goes back to the end of the queue
                    # for the next round of voting.
                    queue.append(current_senator)

            # Process Radiant senator
            else:
                if r_banned:
                    # There is a pending ban against Radiant. This senator is eliminated.
                    r_banned -= 1
                    r_count -= 1
                else:
                    # No pending ban against Radiant. This senator is eligible to vote.
                    # Greedily issue a ban against the next available Dire senator.
                    d_banned += 1
                    # After voting, the senator goes back to the end of the queue
                    # for the next round of voting.
                    queue.append(current_senator)

        # If Radiant count is non-zero, they win; otherwise Dire wins.
        return "Radiant" if r_count else "Dire"
