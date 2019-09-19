import turtle
import sys
import os

screen = turtle.Screen()
screen.title("PONG MADNESS")
screen.bgcolor("black")
screen.setup(720,480)

#desenhando a bola
ball = turtle.Turtle("circle")
ball._tracer(0)
ball.color("red")
ball.penup()

# variáveis utilizadas no players
player_height = 6
player_width = 1.5

# parâmetros do p1
player1 = turtle.Turtle("square")
player1._tracer(0)
player1.setx(-300)
player1.turtlesize(player_height, player_width)
player1.color("gray")

# parâmetro do p2
player2 = turtle.Turtle("square")
player2._tracer(0)
player2.setx(300)
player2.turtlesize(player_height, player_width)
player2.color("gray")

player1.penup()
player2.penup()

# Variáveis de movimentação dos pjs
p_speed = 42

# Movimentação do p1
def p1_up():
    y = player1.ycor()
    y += p_speed
    player1.sety(y)

def p1_down():
    y = player1.ycor()
    y -= p_speed
    player1.sety(y)

# Movimentação do p2
def p2_up():
    y = player2.ycor()
    y += p_speed
    player2.sety(y)

def p2_down():
    y = player2.ycor()
    y -= p_speed
    player2.sety(y)


# Recebendo a entrada de movimentos dos pjs
screen.onkeypress(p1_up, 'w')
screen.onkeypress(p1_down, 's')
screen.onkeypress(p2_up, 'Up')
screen.onkeypress(p2_down, 'Down')

screen.listen()

# parâmetros de movimento da bola
y_ac = 1
x_ac = 1
b_speed = 0.5

while True:  
    # movimentação da bola
    y = ball.ycor()
    x = ball.xcor()
    y += b_speed*y_ac
    x += b_speed*x_ac

    if (ball.ycor() >= 240):
        y_ac =-1
        ball.sety(y)

    if (ball.ycor() <= -240):
        y_ac = 1
        ball.sety(y)

    if (ball.xcor() >= 360): 
        x_ac = -1
        ball.setx(x)

    if (ball.xcor() <= -360):
        x_ac = 1
        ball.setx(x)

    ball.goto(x,y)

    # atualização da tela
    screen.update()
