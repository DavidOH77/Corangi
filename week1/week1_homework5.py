players = ['황의조', '황희찬', '구자철', '이재성', '기성용']

for player in players:
    print(player)

print('*' * 30)

a = input('OUT 시킬 선수 번호 : ')
del players[int(a)]

b = input('IN 할 선수 이름 : ')
players.append(b)

print('*' * 30)


print('교체 결과 : ')
for player in players:
    print(player)