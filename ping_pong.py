import numpy as np
import functools
import json

names = ['Ana','Jose','Juan']
# ana = 0
# jose = 1
# juan = 2

print('Players: ', names)
print('')

posibilities = [
    [1,2,0],
    [2,0,1],
    [0,1,2]
]  

for i in posibilities:
    player_1 = i[0]
    player_2 = i[1]
    benched_player = i[2]

    remaining_matches = [17, 15, 10]
    matches = int(functools.reduce(lambda a, b: a+b, remaining_matches)/2)

    history = []
    winner = ''
    loser = ''

    for k in range(0,matches):
        win = np.argmax([remaining_matches[player_1], remaining_matches[player_2]])
        remaining_matches[player_1] -= 1
        remaining_matches[player_2] -= 1
        if win == 0: 
            winner = names[player_1]
            loser = names[player_2]
        else:
            winner = names[player_2]
            loser = names[player_1]
        history.append({'Match': k+1, 'player_1': names[player_1], 'player_2': names[player_2], 'winner': winner, 'loser': loser})
        
        if win == 0: 
            aux = benched_player    
            benched_player = player_2 
            player_2 = aux 
            winner = names[player_1]
        else:
            aux = benched_player
            benched_player = player_1
            player_1 = aux
            winner = names[player_2]

    if remaining_matches == [0,0,0]:
        result = {'2nd_match_loser': history[1]['loser'], 'history': history }
        json_result = json.dumps(result, indent=4)
        print(json_result,  file=open('ping_pong_result.json', 'wt'))
        print('2nd match loser: ', history[1]['loser'])
        print('History of matches exported in ping_pong_result.json')
        break
