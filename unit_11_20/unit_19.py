'''연습'''
for i in range(5):
  for j in range(5):
    if j<i:
      print(' ', end='')  ##' '는 왜??
    else:
      print('*', end='')
  print()

'''심사'''
a = int(input())
ast = 1
for i in range(a):
    print(' '*(a-1),'*'*ast)
    a -= 1
    ast += 2