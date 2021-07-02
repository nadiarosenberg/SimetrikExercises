import numpy as np
import functools

names = ['Ana','Jose','Juan']
remaining_matches = [17, 15, 10]

player_1 = 0 #Ana
player_2 = 1 #Jose
benched_player = 2 #Juan

matches = int(functools.reduce(lambda a, b: a+b, remaining_matches)/2)

print('Jugadores', names)
print('Partidos restantes', remaining_matches)
print('')

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
    history.append({"player_1": names[player_1], "player_2": names[player_2], "winner": winner, "loser": loser})
    
    if win == 0: #if player_1 wins
        aux = benched_player   # Aux es Juan 
        benched_player = player_2 # benched_player es Jose
        player_2 = aux #player_2 es Juan 
        winner = names[player_1]
    else:
        aux = benched_player
        benched_player = player_1
        player_1 = aux
        winner = names[player_2]

print('2nd match loser: ', history[1]['loser'])
print(history)
