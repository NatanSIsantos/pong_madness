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
ball.color("blue")
ball.penup()
ball.speed("fastest")

# variáveis utilizadas no players
player_height = 6
player_width = 1.5

# parâmetros do p1
player1 = turtle.Turtle("square")
player1._tracer(0)
player1.setx(-300)
player1.turtlesize(player_height, player_width)
player1.color("white")

# parâmetro do p2
player2 = turtle.Turtle("square")
player2._tracer(0)
player2.setx(300)
player2.turtlesize(player_height, player_width)
player2.color("white")

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



screen.onkey(p1_up,'w')
screen.onkey(p1_down, 's')
screen.onkey(p2_up,'Up')
screen.onkey(p2_down,'Down')
screen.listen()
while True:   
    screen.update()
