from turtle import Turtle
position = [(350,0),(-350,0)]
class paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddles = []
        self.create_paddle()
    
    def create_paddle(self):    
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(5,1,0)
              
    def rup(self):
        self.goto(self.xcor(),self.ycor()+20)

    def rdown(self):
        self.goto(self.xcor(),self.ycor()-20)

    def lup(self):
        self.goto(self.xcor(),self.ycor()+20)

    def ldown(self):
        self.goto(self.xcor(),self.ycor()-20)
