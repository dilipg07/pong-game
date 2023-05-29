from turtle import Turtle
position = [(350,0),(-350,0)]
class paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddles = []
        self.create_paddle()
    
    def create_paddle(self):
        for pos in position:    
            new_paddle = Turtle()
            new_paddle.shape('square')
            new_paddle.color('white')
            new_paddle.penup()
            new_paddle.shapesize(5,1,0)
            new_paddle.goto(pos)
            self.paddles.append(new_paddle)


            
    def rup(self):
        self.paddles[0].goto(self.paddles[0].xcor(),self.paddles[0].ycor()+20)

    def rdown(self):
        self.paddles[0].goto(self.paddles[0].xcor(),self.paddles[0].ycor()-20)

    def lup(self):
        self.paddles[1].goto(self.paddles[1].xcor(),self.paddles[1].ycor()+20)

    def ldown(self):
        self.paddles[1].goto(self.paddles[1].xcor(),self.paddles[1].ycor()-20)