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
    user_ans = input('type_the_name\n')
    return user_ans.upper()

def get_test_ans(test_player):
    test_ans = str(test_player.get('team_id')[0])
    return test_ans

def show_result(points,count):
    print("you have {} points".format(points))
    print("you have answered {} questions".format(count))

points,count = 0,0

while count <3:
    count +=1
    test_player = preprocess()
    user_ans = get_user_ans()
    test_ans = get_test_ans(test_player)
    if len(user_ans) != 3:
        print("Please type the 3-letter abreviation of the team:")
        user_ans = get_user_ans()
    elif user_ans == test_ans:
        print('you are right!')
        print('He is from team {}'.format(test_ans))
        points+=1
    else:
        print('you type',user_ans, type(user_ans))
        print("You type the wrong team, the name of the team is {}".format(test_ans))

    show_result(points, count)
