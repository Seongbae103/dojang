# 람다 표현식 
## 1. 람다 표현식으로 함수 만들기
> lambda 매개변수들 : 식
### 1.1 람다 표현식 자체를 호출
- 변수에 할당하지 않고 람다식 자체를 호출 가능
> (lambda 매개변수들:식)(인수들)
### 1.2 람다식 안에는 변수 생성 불가
- 단, 식 밖의 변수는 사용할 수 있다
> - (lambda x : y=10; x+y)(1) : X 
> - (lambda x : x+y)(1) : O 

### 1.3 람다식을 인수로 사용
- map이 대표적이다

    
    - x = [1,2,3]
    - def plus(x): return x+10
    - list(map(plus, [1,2,3]))
    - = [11, 12, 13]

    == list(map(lambda x : x + 10, [1, 2, 3]))
    
## 2. 람다식과 map, filter, reduce 함수 활용
### 2.1 람다 표현식에 조건부 표현식 사용
> lambda 매개변수들:식1 if 조건식 else 식2
- 람다식에서 if흫 사용했다면 반드시 else를 사용
- 조건식이 True일 때, 식1
- 조건식이  False일 때, 식2

- 람다식 내부에는 elif 사용이 불가 (아래 경우처럼 if를 연속으로 사용)
    > lambda 매개변수들:식1 if 조건식 else 식2 if 조건식 else 식3

### 2.2 map에 객체 여러 개 넣기
- map은 리스트 등의 반복 가능한 객체를 여러 개 넣을 수 있다

### 2.3 filter 사용
- 반복 가능한 객체에서 반환값이 True일 때 특정 조건에 맞는 요소만 가져오는 함수
    > filter(함수, 반복가능한객체)
- 예시
    

     ls = []
     [filter(lambda x: x>5, ls)]

### 2.4 reduce 사용
- 반복 가능한 객체의 각 요소를 지정된 함수로 처리하고 이전 결과에 누적해서 반환하는 함수
    > from functools import reduce
    > reduce(함수, 반복가능한객체)
- 예시

    
    def f(x, y): return x+y
    ls = [1,2,3,4,5]
    reduce(f, als) ==((((1+2)+3)+4)+5) == 15
- 람다식
    > reduce(lambda x, y: x+y, ls)