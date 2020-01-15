pay = input("시급을 입력해주세요 : ")
pay = int(pay)

if pay > 8350:
    print('적절한 시급입니다 :) ')
else:
    print("최저임금보다 적어요 :( ")

print('='*50)

numbers = [7, 2, 3 ,1 ,10, 6, 4, 9, 8, 5]

for i in numbers:
    if i >5:
        print(i)
    else:
        print(i, "*")

print('=' * 50)
