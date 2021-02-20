import pandas as pd

# Preprocess data
print('==NBA, where amazing happens==')
data = pd.read_csv('data/nba_lottery_picks_data.csv', nrows=1000)
data = data.drop(columns=['Unnamed: 0'], axis=1)
random_player = data.sample()


def save_nba_player_to_dict(player):
    return player.to_dict('list')


def announcement(test_player):
    pick_overall = test_player.get('pick_overall')
    year = test_player.get('Year')
    player_name = test_player.get('player')
    print("With the {} pick of the {} NBA draft, which team select {}".format(pick_overall, year, player_name ))


def preprocess():
    random_player = data.sample()
    test_player = save_nba_player_to_dict(random_player)
    announcement(test_player)
    return test_player


def get_user_ans():
    user_ans = input('type the name of the TEAM in 3 UPPERLETTER:\n')
    return user_ans.upper()

def get_num_participants():
    num_participants = int(input('how many Users want to play\n'))
    return num_participants

def get_user_name(num_participants):
    user_name_list = []
    for i in range(num_participants):
        print('Hi, player {}, please type your name:\n'.format(i+1))
        user_name = str(input('Type your name here!\n'))
        user_name_list.append(user_name)
    return user_name_list

def get_rounds():
    rounds = int(input('how many rounds you wanna play?\n'))
    return rounds


def get_test_ans(test_player):
    test_ans = str(test_player.get('team_id')[0])
    return test_ans

def show_result(result,user_name_list,rounds):
    for i in range(len(user_name_list)):
        print('=====')
        print('player {}'.format(user_name_list[i]))
        print("you have {} points".format(result[user_name_list[i]]))
        print("you have answered {} questions".format(rounds))
        print('=====')


def reset(points,count):
    points, count = 0, 0
    return points, count




# start of the game, decide the number of players and their names
points, count = reset(points=0,count=0)
num_participants = get_num_participants()
user_name_list = get_user_name(num_participants)
result = {}
rounds  = get_rounds()


for i in range(num_participants):
    print('-----')
    print('Game start for player {}'.format(user_name_list[i]))
    print('-----')
    while count < rounds:
        count += 1
        test_player = preprocess()
        user_ans = get_user_ans()
        test_ans = get_test_ans(test_player)
        if len(user_ans) != 3:
            print('=====')
            print("Please type the 3-letter abreviation of the team:")
            user_ans = get_user_ans()
            print('=====')
        elif user_ans == test_ans:
            print('=====')
            print('you are right!')
            print('He is from team {}'.format(test_ans))
            print('=====')
            points+=1
        else:
            print('=====')
            print('you type',user_ans, type(user_ans))
            print("You type the wrong team, the name of the team is {}".format(test_ans))
            print('=====')
    result[user_name_list[i]] = points
    points,count = reset(points,count)
show_result(result,user_name_list,rounds)

