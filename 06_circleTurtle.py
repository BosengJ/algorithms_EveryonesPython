import turtle as t
t.shape('turtle')

n = 50              # circle 50개
t.bgcolor('black')
t.color('green')
t.speed(0)          # 최고속도:0, 최저 속도:1, 빠른속도:10

for i in range(n):
    t.circle(80)    # r=80, circle
    t.left(360/n)   # 거북이가 360/n 만큼 회전한다. 즉, 50개의 써클을 돌리면서 360도에서 50으로 나눈 간격만큼 각도가 벌려지면서 그려진다.