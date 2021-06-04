import turtle as t
import random

t.shape('turtle')
t.speed(0)

for i in range(500):
    a = random.randint(1,300)
    b = random.randint(1,20)
    t.setheading(a)
    t.forward(b)