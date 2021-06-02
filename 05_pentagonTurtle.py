import turtle as t
t.shape('turtle')

n = 5               #오각형
t.color('purple')
t.begin_fill()      #색칠 영역 시작

for i in range(n):
    t.forward(200)
    t.left(360/n)
t.end_fill()        #색칠 영역 마무리