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


def runoff(voters):
    voters_list = voters.copy()

    while True:

        first_place_list = [voter[0] for voter in voters_list if voter]

        count_dict = {vote: first_place_list.count(vote) for vote in first_place_list}

        winner = None
        max_count = 0
        min_count = min(count_dict.values()) if count_dict else 0
        less_voted_candidates_list = [candidate for candidate, quantity in count_dict.items() if quantity <= min_count]

        for candidate, quantity in count_dict.items():
            if quantity > max_count:
                max_count = quantity
                winner = candidate

        if winner:
            if count_dict[winner] > (sum(count_dict.values()) / 2):
                break
            else:
                for candidate in voters[0]:
                    if candidate not in first_place_list:
                        less_voted_candidates_list.append(candidate)
                for voter in voters_list:
                    for candidate in less_voted_candidates_list:
                        voter.pop(voter.index(candidate))
        else:
            break

    return winner


if __name__ == '__main__':
    voters = [["dem", "ind", "rep"],
              ["rep", "ind", "dem"],
              ["ind", "dem", "rep"],
              ["ind", "rep", "dem"]]

    print(runoff(voters))  # should return  "ind"

    voters = [["a", "c", "d", "e", "b"],
              ["e", "b", "d", "c", "a"],
              ["d", "e", "c", "a", "b"],
              ["c", "e", "d", "b", "a"],
              ["b", "e", "a", "c", "d"]]

    print(runoff(voters))  # should return None

    list1 = [['a', 'c', 'b', 'd', 'e'],
             ['d', 'c', 'a', 'b', 'e'],
             ['e', 'b', 'd', 'a', 'c'],
             ['e', 'a', 'b', 'c', 'd'],
             ['b', 'c', 'e', 'a', 'd']]

    print(runoff(list1))  # should return 'e'
