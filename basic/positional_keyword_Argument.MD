# 함수에서 위치인수와 키워드 인수 사용하기
## 1. 위치인수와 리스트 언패킹
> 위치 인수와 언패킹은 인수의 수가 정해지지 않은 가변 인수에 사용한다
### 1.1 위치 인수
    > 함수에 인수를 순서대로 넣는 방식
### 1.2 언패킹
> 함수(*튜플) 
> 함수(*리스트)
### 1.3 가변 인수 함수 생성
    def 함수명(*매개변수):
        코드
    <a style=color:red>'*매개변수'는 항상 매개변수 순서에서 가장 뒤에 있어야 한다
## 2. 키워드 인수
    > 함수(키워드='값)
    - seq, end도 키워드 인수다

## 3. 딕셔너리 언패킹
    > 함수(**딕셔너리)
<a style=color:red>※</a> 딕셔너리의 키는 반드시 문자열
- 딕셔너리를 언패킹하면 value가 인수로 들어간다
- 매개 변수의 수나 이름이 다른 경우 에러가 발생한다
### 3.1 왜 **를 두 번 쓰나?
> 딕셔너리는 key:value의 쌍 형태로 저장되는 형태라서 애스터리스크(*)를 한 번만 사용하게 되면 key만 인수가 된다

### 3.2 키워드 인수(kwargs)를 사용하는 가변 인수 함수 생성
    def 함수(**매개변수)
        코드
## 4. 매개변수에 초깃값 지정
    def 함수(매개변수=값)
        코드
### 4.1 초깃값을 지정한 매개변수의 위치
> 초깃값이 지정된 매개변수 뒤에 초깃값 없는 매개변수가 들어갈 위치를 알 수 없기 때문에 초깃값이 지정된 매개변수는 뒤로 몰아준다

