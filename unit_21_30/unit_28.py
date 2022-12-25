'''
연습
n = int(input())
text = input()
words = text.split()

if (len(words) < n):
    print('wrong')
else:
    n_gram = [text[i:] for i in range(n)]
    for i in n_gram:
        print(i)
'''

#심사는 집에서 책보고 추가