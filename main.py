from turtle import Screen, Turtle
from Paddle import paddle
from Ball import ball
import time
from Scoreboard import scoreboard

screen = Screen()
screen.title("Pong")
screen.tracer(0) 
screen.bgcolor('black')
screen.setup(800,600)
score = scoreboard()
rpaddle = paddle()
rpaddle.goto(350,0)
lpaddle = paddle()
lpaddle.goto(-350,0)
bal = ball()
screen.listen()
screen.onkey(rpaddle.rup,'Up')
screen.onkey(rpaddle.rdown,'Down')
screen.onkey(lpaddle.lup,'w')
screen.onkey(lpaddle.ldown,'s')

game_on = True
while game_on:
    screen.update()
    time.sleep(bal.move_speed)
    bal.move()
    # Datetct collision with wall
    if bal.ycor() > 280 or bal.ycor() < -280:
        bal.bounce_y()
    # Detect collisionn with paddle
    if (bal.distance(rpaddle)< 60 and bal.xcor() > 320) or (bal.distance(lpaddle)< 60 and bal.xcor() < -320):
        bal.bounce_x()
    # Detect r paddle misses
    if bal.xcor() > 380:
        bal.reset_position()
        score.l_point()
        score.update_scoreboard()
    # Detect l paddle misses
    if bal.xcor() < -380:
        bal.reset_position()
        score.r_point()
        score.update_scoreboard()