a = int(input())
b = int(input())
divisor = set()
for i in range(1, a+1):
    if a % i == 0:
        divisor.add(i)
for j in range(1, b+1):
    if b % i == 0:
        divisor.add(i)

divisor = a&b
result = 0 
if type(divisor) == set:
    result = sum(divisor)
print(result)

# 딕셔너리에서 :이 없으면 세트??