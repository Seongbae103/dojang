'''
연습
maria = {'korean': 94, 'english':91,'math':89, 'science':83}
avg = sum(maria.values())/len(maria)
print(avg)'''

'''
입력 :
alpha bravo charlie delta
10 20 30 40
'''
'''
# 심사
# 두 리스트로 딕셔너리를 만들고 키가 ? 값이 !인 아이템은 제거된 딕셔너리를 출력
a = input().split()
b = map(int, input().split())
x = dict(zip(a,b))
del x['alpha']
x = {key:value for key, value in x.items() if value != 30}

print(x)
'''