import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Preprocess data
print('==NBA, where amazing happens==')
data = pd.read_csv('data/nba_lottery_picks_data.csv',nrows=1000)
data = data.drop(columns=['Unnamed: 0'],axis=1)


random_player = data.sample()
def save_nba_player_to_dict(player):
    return player.to_dict('list')


def announcement(test_player):
    print("With the {} pick of the {} NBA draft, which team select {}".format(test_player.get('pick_overall'),test_player.get('Year'),test_player.get('player')))

random_player = data.sample()
test_player = save_nba_player_to_dict(random_player)



# x = input('please type hi')
# if x == 'hi':
#     print('hey')
test_player = save_nba_player_to_dict(random_player)
announcement(test_player)
user_ans = input('type_the_name')
test_ans = str(test_player.get('team_id')[0])
#check ans
if len(user_ans)!=3:
    print("Please type the 3-letter abreviation of the team:")
    user_ans = input('type_the_name')
elif user_ans == test_ans:
    print('you are right!')
else:
    print('you type',user_ans,type(user_ans))
    print('the ans is ',str(test_ans),len(test_ans))
    print("You type the wrong team, the name of the team is {}".format(test_ans))










