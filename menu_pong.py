import turtle
import sys
import os
from pong_1jogador import pong_1player
from pong_2jogadores import pong_2players
import time
import simpleaudio as sa


def selection_sound():
    filename = 'selection.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()


# Interface
screen = turtle.Screen()
screen.title("PONG MADNESS")
screen.bgcolor("black")
screen.setup(720, 480)
screen.tracer(0)

# Título do jogo
game_title = turtle.Turtle("square")
game_title.speed(0)
game_title.color("white")
game_title.penup()
game_title.hideturtle()
game_title.goto(0, 180)
game_title.write("PONG MADNESS", align="center",
             font=("Press Start 2P", 24, "normal"))

# Tela de seleção
mode = turtle.Turtle("square")
mode.speed(0)
mode.color("white")
mode.penup()
mode.hideturtle()
mode.goto(0, 50)
mode.write("modeS DE JOGO", align="center",
           font=("Press Start 2P", 16, "normal"))

mode = turtle.Turtle("square")
mode.speed(0)
mode.color("white")
mode.penup()
mode.hideturtle()
mode.goto(0, 10)
mode.write("1P", align="center",
           font=("Press Start 2P", 16, "normal"))

mode = turtle.Turtle("square")
mode.speed(0)
mode.color("white")
mode.penup()
mode.hideturtle()
mode.goto(0, -30)
mode.write("2P", align="center",
           font=("Press Start 2P", 16, "normal"))

# Parâmetros da seleção
selection = turtle.Turtle("square")
selection.speed(0)
selection.turtlesize(1.5, 6)
selection.color('blue')
selection.fillcolor('')
selection.penup()
selection.sety(25)


def selection_up():
    selection.sety(25)
    selection_sound()


def selection_down():
    selection.sety(-15)
    selection_sound()


def selection_mode():
    if (selection.ycor() == 25):
        screen.clear()
        pong_1player()

    if (selection.ycor() == -15):
        screen.clear()
        pong_2players()


screen.onkeypress(selection_mode, 'Return')
screen.onkeypress(selection_up, 'Up')
screen.onkeypress(selection_down, 'Down')
screen.listen()

while(True):
    screen.update()
