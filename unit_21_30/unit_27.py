'''
# 연습
with open('27_words_1.txt', 'r') as file:
    count = 0
    txts = file.readlines()
    for i in txts:
        if len(i.strip('\n'))<= 10:
            count += 1
    print(count)
'''

# 심사
with open('27_words_2.txt', 'r') as file:
    txts = file.readline()
    txt = txts.split()
    for i in txt:
        if 'c' in i:
            print(i.strip(',.'))