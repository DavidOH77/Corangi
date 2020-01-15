data = ['조회수 : 1,500', '조회수 : 1,002', '조회수 : 300', '조회수 : 251'
        , '조회수 : 13,432', '조회수 : 998']

sum = 0

# Level1

for one_data in data:
    print(one_data)

# Level2

for one_data in data:
    one_data = one_data.replace('조회수 : ', '')
    print(one_data)

# Level3

for one_data in data:
    one_data = one_data.replace('조회수 : ', '').replace(',', '')
    one_data = int(one_data)
    sum = sum + one_data
    print(sum)

print('합계 :',sum)
