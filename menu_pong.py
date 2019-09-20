import turtle
import sys
import os
from pong import pong

# Interface
screen = turtle.Screen()
screen.title("PONG MADNESS")
screen.bgcolor("black")
screen.setup(720, 480)
screen.tracer(0)

# Título do jogo
titulo = turtle.Turtle("square")
titulo.speed(0)
titulo.color("white")
titulo.penup()
titulo.hideturtle()
titulo.goto(0, 180)
titulo.write("PONG MADNESS", align="center",
             font=("Press Start 2P", 24, "normal"))

# Tela de seleção
modo = turtle.Turtle("square")
modo.speed(0)
modo.color("white")
modo.penup()
modo.hideturtle()
modo.goto(0, 50)
modo.write("MODOS DE JOGO", align="center",
           font=("Press Start 2P", 16, "normal"))

modo = turtle.Turtle("square")
modo.speed(0)
modo.color("white")
modo.penup()
modo.hideturtle()
modo.goto(0, 10)
modo.write("1P", align="center",
           font=("Press Start 2P", 16, "normal"))

modo = turtle.Turtle("square")
modo.speed(0)
modo.color("white")
modo.penup()
modo.hideturtle()
modo.goto(0, -30)
modo.write("2P", align="center",
           font=("Press Start 2P", 16, "normal"))

# Parâmetros da seleção
selecao = turtle.Turtle("square")
selecao.speed(0)
selecao.turtlesize(1.5, 6)
selecao.color('blue')
selecao.fillcolor('')
selecao.penup()
selecao.sety(25)


def selecao_up():
    selecao.sety(25)


def selecao_down():
    selecao.sety(-15)


def selecao_modo():
    if (selecao.ycor() == -15):
        screen.clear()
        pong()


screen.onkeypress(selecao_modo, 'Return')
screen.onkeypress(selecao_up, 'Up')
screen.onkeypress(selecao_down, 'Down')
screen.listen()

while(True):
    screen.update()
