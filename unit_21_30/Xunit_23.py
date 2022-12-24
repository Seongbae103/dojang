'''
연습문제
a = [[[0 for i in range(3)] for i in range(4)] for i in range(2)]
print(a)
'''
row, col = map(input().split())
matrix = [[i for i in range(row)] for i in range(col)]

print(matrix)