'''연습문제
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = [i for i in a if len(i)==5]

print(b)'''

'''심사
a, b = map(int, input().split())
x = [2 ** i for i in range(a, b+1) if 1 <= a <= 20 and 10 <= b <= 30]
del x[1]
del x[-2]
print(x)'''