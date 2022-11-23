'''연습'''
i= 0
while True:
  if i % 10 != 3:
    i += 1
    continue
  if i > 73: break
  print(i, end = ' ')
  i +=1

'''심사'''
a, b = map(int, input().split())
i = a

while True:
  if i % 10 == 3:
    i+=1
    continue
  if i>b:
    break
  print(i, end = ' ')
  i+=1