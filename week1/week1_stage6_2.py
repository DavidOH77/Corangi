players = ['황의조', '황희찬', '구자철', '이재성', '기성용']

print(players)
print(players[0])
print(players[3])

print(players[-1])
print(players[-5])

small_players = players[1:3]
print(small_players)

small_players = players[-4:-1]
print(small_players)

small_players = players[3:]
print(small_players)

small_players = players[:4]
print(small_players)

players.append("이승우")
print(players)
players.append("김민재")
print(players)

del players[1]
del players[1]

print(players)
print(len(players))