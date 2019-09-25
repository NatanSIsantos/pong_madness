import turtle
import random
import sys
import os
import time
import simpleaudio as sa


def pong_1player():

    def pong_sound():
        filename = 'pong.wav'
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()

    screen = turtle.Screen()
    screen.title("PONG MADNESS")
    screen.bgcolor("black")
    screen.setup(720, 480)
    screen.tracer(0)

    # desenhando a bola
    ball = turtle.Turtle("circle")
    ball.speed(0)
    ball.color("red")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.2
    ball.dy = 0.2

    # variáveis utilizadas no players
    player_height = 5
    player_width = 1

    # parâmetros do p1
    player1 = turtle.Turtle("square")
    player1.speed(0)
    player1.turtlesize(player_height, player_width)
    player1.color("blue")
    player1.penup()
    player1.setx(-350)

    # parâmetro da máquina
    maquina = turtle.Turtle("square")
    maquina.speed(0)
    maquina.turtlesize(player_height, player_width)
    maquina.color("blue")
    maquina.penup()
    maquina.setx(340)

    # pontuação
    score_1 = 0
    score_2 = 0

    # display de pontuação
    placar = turtle.Turtle("square")
    placar.speed(0)
    placar.color("white")
    placar.penup()
    placar.hideturtle()
    placar.goto(0, 180)
    placar.write("0 : 0", align="center", font=(
        "Press Start 2P", 24, "normal"))

    # display de vitoria
    vitoria = turtle.Turtle("square")
    vitoria.speed(0)
    vitoria.color("green")
    vitoria.penup()
    vitoria.hideturtle()
    vitoria.goto(0, 0)

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

    # Movimentação da Máquina

    def machine_p2():
        reaction_chance = random.randint(0, 100)
        if (reaction_chance >= 97):
            if (ball.ycor() > maquina.ycor()):
                y = maquina.ycor()
                y += 0.25*p_speed
                maquina.sety(y)
            if (ball.ycor() < maquina.ycor()):
                y = maquina.ycor()
                y -= 0.25*p_speed
                maquina.sety(y)
        elif (reaction_chance < 99):
            y = maquina.ycor()
            maquina.sety(y)

    # Recebendo a entrada de movimentos dos pjs
    screen.onkeypress(p1_up, 'w')
    screen.onkeypress(p1_down, 's')

    screen.listen()

    while True:
        # movimentação da máquina
        machine_p2()

        # movimentação da bola
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # colisão da bola com parede superior
        if (ball.ycor() > 225):
            ball.sety(225)
            ball.dy *= -1
            pong_sound()

        # colisão da bola com parede inferior
        if (ball.ycor() < -225):
            ball.sety(-225)
            ball.dy *= -1
            pong_sound()

        # colisão da bola com parede direita
        if (ball.xcor() > 360):
            score_1 += 1
            placar.clear()
            placar.write("{} : {}".format(score_1, score_2),
                         align="center", font=("Press Start 2P", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1
            if (ball.dx > 0):
                ball.dx = 0.2
            elif (ball.dx < 0):
                ball.dx = -0.2
            ball.dy = 0.2

        # colisão da bola com parede esquerda
        if (ball.xcor() < -360):
            score_2 += 1
            placar.clear()
            placar.write("{} : {}".format(score_1, score_2),
                         align="center", font=("Press Start 2P", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1
            if (ball.dx > 0):
                ball.dx = 0.2
            elif (ball.dx < 0):
                ball.dx = -0.2
            ball.dy = 0.2

        # colisão da bola com o player 1
        if (ball.xcor() < -330 and ball.ycor() < player1.ycor() + 65 and
                ball.ycor() > player1.ycor() - 65 and
                ball.xcor() > -331):
            ball.dx *= -1
            if (ball.dx > 0):
                ball.dx += 0.01
            elif (ball.dx < 0):
                ball.dx -= 0.01

            # divisão de setores
            if (ball.ycor() <= player1.ycor() + 5 and
                    ball.ycor() >= player1.ycor() - 5):
                if (ball.dy > 0):
                    ball.dy = ball.dx
                elif (ball.dy < 0):
                    ball.dy = -ball.dx

            elif (ball.ycor() > player1.ycor() + 5 and
                  ball.ycor() <= player1.ycor() + 20):
                if (ball.dy > 0):
                    ball.dy = ball.dx + 0.02
                elif (ball.dy < 0):
                    ball.dy = -ball.dx - 0.02

            elif (ball.ycor() < player1.ycor() - 5 and
                  ball.ycor() >= player1.ycor() - 20):
                if (ball.dy > 0):
                    ball.dy = ball.dx + 0.02
                elif (ball.dy < 0):
                    ball.dy = -ball.dx - 0.02

            elif (ball.ycor() > player1.ycor() + 20 and
                  ball.ycor() <= player1.ycor() + 35):
                if (ball.dy > 0):
                    ball.dy = ball.dx + 0.03
                elif (ball.dy < 0):
                    ball.dy = -ball.dx - 0.03

            elif (ball.ycor() < player1.ycor() - 20 and
                  ball.ycor() >= player1.ycor() - 35):
                if (ball.dy > 0):
                    ball.dy = ball.dx + 0.03
                elif (ball.dy < 0):
                    ball.dy = -ball.dx - 0.03

            elif (ball.ycor() > player1.ycor() + 35 and
                  ball.ycor() <= player1.ycor() + 50):
                if (ball.dy > 0):
                    ball.dy = ball.dx + 0.04
                elif (ball.dy < 0):
                    ball.dy = -ball.dx - 0.04

            elif (ball.ycor() < player1.ycor() - 35 and
                  ball.ycor() >= player1.ycor() - 50):
                if (ball.dy > 0):
                    ball.dy = ball.dx + 0.04
                elif (ball.dy < 0):
                    ball.dy = -ball.dx - 0.04

            elif (ball.ycor() > player1.ycor() + 50 and
                  ball.ycor() <= player1.ycor() + 65):
                if (ball.dy > 0):
                    ball.dy = ball.dx + 0.05
                elif (ball.dy < 0):
                    ball.dy = -ball.dx - 0.05

            elif (ball.ycor() < player1.ycor() - 50 and
                  ball.ycor() >= player1.ycor() - 65):
                if (ball.dy > 0):
                    ball.dy = ball.dx + 0.05
                elif (ball.dy < 0):
                    ball.dy = -ball.dx - 0.05
            pong_sound()

        # colisão da bola com a máquina
        if (ball.xcor() > 320 and ball.ycor() < maquina.ycor() + 65 and
                ball.ycor() > maquina.ycor() - 65 and
                ball.xcor() < 321):
            ball.dx *= -1
            if (ball.dx > 0):
                ball.dx += 0.01
            elif (ball.dx < 0):
                ball.dx -= 0.01

            # divisão de setores
            if (ball.ycor() <= maquina.ycor() + 5 and
                    ball.ycor() >= maquina.ycor() - 5):
                if (ball.dy > 0):
                    ball.dy = -ball.dx
                elif (ball.dy < 0):
                    ball.dy = ball.dx

            elif (ball.ycor() > maquina.ycor() + 5 and
                  ball.ycor() <= maquina.ycor() + 20):
                if (ball.dy > 0):
                    ball.dy = -ball.dx + 0.02
                elif (ball.dy < 0):
                    ball.dy = ball.dx - 0.02

            elif (ball.ycor() < maquina.ycor() - 5 and
                  ball.ycor() >= maquina.ycor() - 20):
                if (ball.dy > 0):
                    ball.dy = -ball.dx + 0.02
                elif (ball.dy < 0):
                    ball.dy = ball.dx - 0.02

            elif (ball.ycor() > maquina.ycor() + 20 and
                  ball.ycor() <= maquina.ycor() + 35):
                if (ball.dy > 0):
                    ball.dy = -ball.dx + 0.03
                elif (ball.dy < 0):
                    ball.dy = ball.dx - 0.03

            elif (ball.ycor() < maquina.ycor() - 20 and
                  ball.ycor() >= maquina.ycor() - 35):
                if (ball.dy > 0):
                    ball.dy = -ball.dx + 0.03
                elif (ball.dy < 0):
                    ball.dy = ball.dx - 0.03

            elif (ball.ycor() > maquina.ycor() + 35 and
                  ball.ycor() <= maquina.ycor() + 50):
                if (ball.dy > 0):
                    ball.dy = -ball.dx + 0.04
                elif (ball.dy < 0):
                    ball.dy = ball.dx - 0.04

            elif (ball.ycor() < maquina.ycor() - 35 and
                  ball.ycor() >= maquina.ycor() - 50):
                if (ball.dy > 0):
                    ball.dy = -ball.dx + 0.04
                elif (ball.dy < 0):
                    ball.dy = ball.dx - 0.04

            elif (ball.ycor() > maquina.ycor() + 50 and
                  ball.ycor() <= maquina.ycor() + 65):
                if (ball.dy > 0):
                    ball.dy = -ball.dx + 0.05
                elif (ball.dy < 0):
                    ball.dy = ball.dx - 0.05

            elif (ball.ycor() < maquina.ycor() - 50 and
                  ball.ycor() >= maquina.ycor() - 65):
                if (ball.dy > 0):
                    ball.dy = -ball.dx + 0.05
                elif (ball.dy < 0):
                    ball.dy = ball.dx - 0.05
            pong_sound()

        # colisão do player 1 com as paredes
        if (player1.ycor() > 180):
            player1.sety(180)
        if (player1.ycor() < -180):
            player1.sety(-180)

        # colisão da máquina com as paredes
        if (maquina.ycor() > 180):
            maquina.sety(180)
        if (maquina.ycor() < -180):
            maquina.sety(-180)

        # condição de vitoria player 1
        if (score_1 > 5 and score_1 > score_2 + 1):
            vitoria.write("Vitória", align="center", font=(
                "Press Start 2p", 24, "normal"))
            time.sleep(5)
            vitoria.clear()
            vitoria.hideturtle()
            score_1 = 0
            score_2 = 0
            placar.clear()
            placar.write("0 : 0", align="center", font=(
                "Press Start 2P", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1
            if (ball.dx > 0):
                ball.dx = 0.2
            elif (ball.dx < 0):
                ball.dx = -0.2
            ball.dy = 0.2

        # condição de vitoria da máquina
        if (score_2 > 5 and score_2 > score_1 + 1):
            vitoria.write("Derrota", align="center", font=(
                "Press Start 2p", 24, "normal"))
            time.sleep(5)
            vitoria.clear()
            vitoria.hideturtle()
            score_1 = 0
            score_2 = 0
            placar.clear()
            placar.write("0 : 0", align="center", font=(
                "Press Start 2P", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1
            if (ball.dx > 0):
                ball.dx = 0.2
            elif (ball.dx < 0):
                ball.dx = -0.2
            ball.dy = 0.2
        # atualização da tela
        screen.update()
