# https://www.hackerearth.com/challenge/hiring/superprofs-hiring-challenge/algorithm/the-football-fest-6/

test_cases = int(input())
players = []
for test in range(test_cases):
    first,second = input().split(' ')
    players.append(second)
    back_flag = False
    for j in range(int(first)):
        checks = input().split(' ')
        if len(checks) > 1:
            operation,player = checks[0],checks[1]
            players.append(player)
            if back_flag:
                back_flag = False
        else:
            if back_flag:
                temp = players[-1]
                players.append(last_player)
                last_player = temp
            else:
                last_player = players[-1]
                del players[-1]
                back_flag = True

    print("Player {}".format(str(players[-1])))