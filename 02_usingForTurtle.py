import turtle as t
t.shape('turtle')

# 삼각형 그리기
for i in range(3):
    t.color('red')
    t.forward(200)
    t.left(120)

# 사각형 그리기
for i in range(4):
    t.color('blue')
    t.forward(200)
    t.left(90)

# 원 그리기
t.color('green')
t.circle(100)