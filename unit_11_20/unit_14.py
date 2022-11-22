'''연습'''
written_test = 75
coding_test =  True
if written_test <= 80 and coding_test==True:
    print('합격')
else:
    print('불합격')

'''심사'''
ko, en, ma, sc = map(float, input().split())
avg = (ko + en + ma +sc) /4
if avg >= 80:
    print('합격')
elif avg <0 or avg >100:
    print('잘못된 점수')
else: print('불합격')