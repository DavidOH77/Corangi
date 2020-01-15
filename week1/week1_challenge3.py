a = input("몸무게를 입력해 주세요 : ")
b = input("신장을 입력해 주세요 : ")
a = int(a)
b = int(b)
BMI = (a / (b**2)) * 10000
print ("BMI :", BMI)