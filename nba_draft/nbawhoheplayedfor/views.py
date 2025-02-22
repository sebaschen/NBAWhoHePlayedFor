from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd
import random

def index(request):
    data = pd.read_csv('data/nba_lottery_picks_data.csv', nrows=1000)
    data = data.drop(columns=['Unnamed: 0'], axis=1)
    random_player = data.sample()
    test_player = random_player.to_dict('records')[0]
    announcement = "With the {} pick of the {} NBA draft, which team selected {}".format(
        test_player['pick_overall'], test_player['Year'], test_player['player']
    )
    request.session['test_player'] = test_player
    return render(request, 'nbawhoheplayedfor/index.html', {'announcement': announcement})

def guess(request):
    if request.method == 'POST':
        user_ans = request.POST.get('user_ans')
        test_player = request.session.get('test_player')
        test_ans = test_player['team_id']
        points = request.session.get('points', 0)
        count = request.session.get('count', 0)
        if len(user_ans) != 3:
            return render(request, 'nbawhoheplayedfor/index.html', {'error': 'Please enter a 3-letter team abbreviation.'})
        elif user_ans.upper() == test_ans:
            points += 1
            feedback = 'Correct! He played for {}'.format(test_ans)
        else:
            feedback = 'Wrong! He played for {}'.format(test_ans)
        count += 1
        request.session['points'] = points
        request.session['count'] = count
        return render(request, 'nbawhoheplayedfor/guess.html', {'feedback': feedback, 'points': points, 'count': count})
    else:
        return HttpResponse("Invalid request.")

def result(request):
    points = request.session.get('points', 0)
    count = request.session.get('count', 0)
    del request.session['points']
    del request.session['count']
    return render(request, 'nbawhoheplayedfor/result.html', {'points': points, 'count': count})
