from turtle import *
tracer(0) # выключить анимацию
left(90) # нужно повернуть на ось оординат ( y ) по дефолту направлена на ось абцисс ( x )
k = 20 # задать мастшаб ( по дефолту один я так понял )
screensize(3000, 3000)
for _ in range(9):
    forward(22 * k)
    right(90)
    forward(22 * k)
    right(90)
penup() # поднять хвост
forward(1 * k)
right(90)
forward(5 * k)
left(90)
pendown()
for _ in range(9):
    forward(53 * k)
    right(90)
    forward(75 * k)
    right(90)
penup()
for x in range(-60, 60):
    for y in range(-60, 60):
        goto(x * k, y * k)
        dot(5)
done() # что бы рисунок никуда не ушел