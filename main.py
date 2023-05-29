from turtle import Screen, Turtle
from Pong import paddle



screen = Screen()
screen.title("Pong")
screen.tracer(0) 
screen.bgcolor('black')
screen.setup(800,600)
padle = paddle()
screen.listen()
screen.onkey(padle.rup,'Up')
screen.onkey(padle.rdown,'Down')
screen.onkey(padle.lup,'w')
screen.onkey(padle.ldown,'s')

game_on = True
while game_on:
    screen.update()
screen.exitonclick() 