import turtle as t
'''연습문제'''
n = 5
t.shape('turtle')
for i in range(n):
    t.forward(100)
    t.right((360 / n) * 2)
    t.forward(100)
    t.left(360 / n)

'''심사'''
p, m = map(int, input().split())
t.shape('turtle')
t.speed('fastest')
for i in range(p):
    t.forward(m)
    t.right((360/p)*2)
    t.forward(m)
    t.left(360 / p)

'''p, m = map(int, input().split())
t.shape('turtle')
for i in range(p):
    t.forward(m)
    t.right((360/p)*2)
    t.forward(m)
    t.right(360 / p)
'''
