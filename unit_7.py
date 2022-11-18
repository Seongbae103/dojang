'''연습'''
year = 2000
month = 10
day = 27
hour = 11
minute = 43
second = 59
print(year, month, day, sep ='-', end='') # end=''를 써서 공백을 한 칸 지정해줘야 옆으로 나온다
print(hour, minute, second, sep=':')

'''심사'''
year,month,day,hour,minute,second = input().split()
print(year, month, day, sep='-', end='T')
print(hour, minute, second, sep=':')