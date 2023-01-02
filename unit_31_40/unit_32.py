'''
# 연습
files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']

print(list(filter(lambda x : x.find('.jpg') != False or x.find('.png') != False, files)))
print(list(filter(lambda x : x.find('.jpg') != -1 or x.find('.png') != -1, files)))
print(list(filter(lambda x : x.find('.jpg') == True or x.find('.png') == True, files)))
print(list(filter(lambda x : x.find('.jpg') == 1 or x.find('.png') == 1, files)))

# filter는 반환값이 true일 때만 요소를 가져온다
# x.find('')에서 !=False or !=False로 했을 때 - font가 출력돼서 false여도 나온 경우라 x
# x.find('')에서 !=-1 or !=-1로 했을 때 - 정답
# x.find('')에서 ==True or ==True로 했을 때 - 10.jpg가 없어서 오답
# x.find('')에서 ==1 or ==1로 했을 때 - 10.jpg가 없어서 오답
# 같은 의미 같은데 왜 달라?'''

