# https://www.hackerearth.com/challenge/hiring/superprofs-hiring-challenge/algorithm/the-football-fest-6/
test_cases = int(input())
players = []
for test in range(test_cases):
    first,second = input().split(' ')
    # Initially the player second has the ball
    players.append(second)
    back_flag = False
    # This is to keep track of the last player who had the ball when there was a back attempted otherwise we would not be able to track when the
    # player passed the ball back
    temp = None
    for i in range(int(first)):
        input_values = input().split(' ')
        if len(input_values) > 1:
            operation, player_id = input_values[0], input_values[1]
            players.append(player_id)
            if back_flag:
                back_flag = False
        else:
            if not back_flag:
                temp = players.pop()
                back_flag = True
            else:
                players.append(temp)
                back_flag = False
    print("Player %s" % players[-1])