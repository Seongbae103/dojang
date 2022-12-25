'''
# 연습
a = {i for i in set(range(1, 101)) if i % 3==0}
b = {i for i in set(range(1, 101)) if i % 5==0}
print(a&b)
'''

# 심사
a1,b1 = map(int, input().split())
a = {i for i in range(1, a1+1) if a1%i==0}
b = {i for i in range(1, b1+1) if b1%i==0}

divisor = a & b
result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)