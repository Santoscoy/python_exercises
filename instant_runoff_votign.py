# Your task is to implement a function that calculates an election winner from a list of voter selections using an
# Instant Runoff Voting algorithm. If you haven't heard of IRV, here's a basic overview (slightly altered for this
# kata):
#
# Each voter selects several candidates in order of preference.
# The votes are tallied from the each voter's first choice.
# If the first-place candidate has more than half the total votes, they win.
# Otherwise, find the candidate who got the least votes and remove them from each person's voting list.
# In case of a tie for least, remove all of the tying candidates.
# In case of a complete tie between every candidate, return nil(Ruby)/None(Python)/undefined(JS).
# Start over.
# Continue until somebody has more than half the votes; they are the winner.
# Your function will be given a list of voter ballots; each ballot will be a list of candidates (symbols) in descending
# order of preference. You should return the symbol corresponding to the winning candidate. See the default test for an
# example!


dict = {
    0: {'dem': 3, 'rep': 3, 'ind': 6},  # 3 ind 18 dem 9 rep 9
    1: {'ind': 6, 'dem': 3, 'rep': 3},  # 2 ind 12 dem 6 rep 6
    2: {'rep': 6, 'dem': 6}}            # 1 ind  0 dem 6 rep 6

                                        #   ind 30 dem 21 rep 21


def runoff(voters):
    votes_matrix = {}
    for priority in range(len(voters[0])):
        votes = {}
        for voter in voters:
            for i in range(len(voter)):
                if voter[priority] in votes.keys():
                    votes[voter[priority]] += 1
                else:
                    votes[voter[priority]] = 1

        votes_matrix[priority] = votes

    results = {}
    priority_points = len(voters[0]) + 1
    for priorities, votes in votes_matrix.items():
        priority_points -= 1
        for candidate, vote in votes.items():
            if candidate in results.keys():
                results[candidate] += (vote * priority_points)
            else:
                results[candidate] = vote * priority_points


    return results


if __name__ == '__main__':
    voters = [["dem", "ind", "rep"],
              ["dem", "ind", "rep"],
              ["ind", "dem", "rep"],
              ["ind", "rep", "dem"]]

    print(runoff(voters))  # should return  "ind"

    voters = [["a", "c", "d", "e", "b"],
              ["e", "b", "d", "c", "a"],
              ["d", "e", "c", "a", "b"],
              ["c", "e", "d", "b", "a"],
              ["b", "e", "a", "c", "d"]]
    


    print(runoff(voters))  # should return 'e'
