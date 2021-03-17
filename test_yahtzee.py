from yahtzee_library import *

# The test needs to be wrapped in a function
def test_something():
    num_games = 1000000

    winning_games = list(
        filter(
            lambda x: x == 5,
            [yahtzee() for _ in range(num_games)],
        )
    )
    #print(100 * len(winning_games)/num_games)
    assert abs(len(winning_games)/num_games - 0.046) < 1

