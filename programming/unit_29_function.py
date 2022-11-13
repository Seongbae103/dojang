#연습
x=10
y=3
def get_quotient_remainder(x, y):
    return x//y, x % y
quotient, remainder = get_quotient_remainder(x, y)
print('몫 : {0}, 나머지 : {1}'.format(quotient, remainder))

#심사
x, y = map(int, input().split())
def calc(x, y):
    return x+y, x-y, x*y, x/y

a, s, m, d = calc(x, y)
print('덧셈 : {0}, 뺄셈 : {1}, 곱셈 : {2}, 나눗셈 : {3}'.format(a, s, m, d))