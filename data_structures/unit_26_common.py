#연습문제
a = {i for i in range(1, 101) if i % 3 == 0}
b = {i for i in range(1, 101) if i % 5 == 0}
print(a & b)

#심사문제
num1 = int(input())
num2 = int(input())
a = {i for i in range(1, num1+1) if num1 % i ==0}
b = {i for i in range(1, num2+1) if num2 % i ==0}

divisor = a&b
result = 0 
if type(divisor) == set:
    result = sum(divisor)
print(result)

# 딕셔너리에서 :이 없으면 세트??