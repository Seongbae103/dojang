def solution_1():
    a, b = map(int, input().split())
    print(a+b)

def solution_2():
    a = 50
    b = 100
    c = None
    print(a)
    print(b)
    print(c)

def solution_3():
    ko, en, ma = map(int, input().split())
    avg = (ko+en+ma)/3
    return avg


if __name__ == '__main__':
    solution_1()
    solution_2()
    solution_3()
