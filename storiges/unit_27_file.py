#연습문제
with open('words.txt', 'r') as file:
    count = 0
    words = file.readlines()
    for word in words:
        if len(word.strip('\n')) <= 10:
            count += 1
    print(count)

####각 단어 끝에 \n이 붙은거니까 len(word)로 쓰지 왜 굳이 len(word.strip('\n')?
### ->'\n'은 생략된거라 빼줘야돼서

#심사문제