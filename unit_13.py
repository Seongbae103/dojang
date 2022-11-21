'''연습'''
x = 5
if x != 10:
    print('ok')

'''심사'''
price = int(input())
cash = input()

if cash == 'Cash3000':
    pay = price - 3000
elif cash == 'Cash5000':
    pay = price - 5000
print(pay)