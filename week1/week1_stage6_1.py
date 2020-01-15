string1 = '브이넥 라이트 다운 베스트'
string2 = '        25,990원       '

print(string1)
print(string2)

print(string1[0])
print(string1[1])
print(string1[2])

print(string1[-1])
print(string1[-2])
print(string1[-3])

print(string2[4])
print(string2[5])

print(string1[0:4])
print(string1[-6:-4])
print(string1[4:10])

print(string1[11:])
print(string1[:7])

print(string2.strip())
print(string2)

string2 = string2.strip().replace(',','')[:-1]
print(string2)