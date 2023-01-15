import turtle
from datetime import time
from random import random

wn=turtle.Screen()
wn.colormode(255)
wn.bgpic('背景.jpg')
wn.setup(1920,1080)

'''wn.register_shape('月亮.gif')
wn.register_shape('星光.gif')
wn.register_shape('liuxing.gif')
#月亮
moon=turtle.Turtle()
moon.shape('月亮.gif')
moon.shapesize(0.2,0.2)
moon.up()
moon.goto(-400,250)'''

#炮竹
firecracker=turtle.Turtle()
firecracker.up()
firecracker.goto(0,-200)
firecracker.lt(90)
firecracker.speed('fastest')
firecracker.color('white')
firecracker.shape('square')
firecracker.shapesize(0.2,0.8)

firworks=[]
shape=['circle','classic','square','triangle','arrow','turtle']
for i in range(25):
    newfirework=turtle.Turtle()
    newfirework.speed('fastest')
    newfirework.up()
    newfirework.ht()
    newfirework.shape('circle')
    newfirework.shapesize(0.5,2.5)
    firworks.append(newfirework)

def set_firworks_shape(apperance):
    for firework in firworks:
        firework.shape(apperance)

firecracker.goto(random.randint(0, 500),-200)

while True:
    high=200
    wn.update()
    firecracker.fd(10)
    for firework in firworks:
        firework.fd(60)
    if firecracker.ycor()==high:
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for firework in firworks:
            firework.color(color)
            firework.goto(firecracker.xcor(),firecracker.ycor())
            firework.seth(random.randint(0, 360))
            firework.showturtle()
    if firecracker.ycor() >= high+5:
        firecracker.goto(random.randint(0, 500),-200)
        set_firworks_shape(random.choice(shape))
    time.sleep(0.05)
