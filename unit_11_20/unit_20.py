'''연습'''
for i in range(1, 101):
    if i % 2 == 0 == i % 11:
        print('FizzBuzz')
    elif i % 2 == 0:
        print('Fizz')
    elif i % 11 == 0:
        print('Buzz')
    else: print(i)

'''심사'''
a, b = map(int, input().split())
1 <= a <= 1000
10 <= b <= 1000
for i in range(a, b+1):
    if i % 5 == 0 == i % 7:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 == 0:
        print('Buzz')
    else: print(i)
