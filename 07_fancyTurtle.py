import turtle as t
t.shape('turtle')
t.bgcolor('black')
t.color('yellow')
t.speed(0)

angle = 89 # 거북이가 왼쪽으로 회전할 각도를 지정한다

for i in range(200):
    t.forward(i) # i 만큼 앞으로 이동한다(실행을 반복하면서 선이 길어짐)
    t.left(angle) # 거북이가 왼쪽으로 89도 회전한다