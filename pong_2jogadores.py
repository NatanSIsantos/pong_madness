import sys
import turtle
import os
import time
import simpleaudio as sa


def pong_2players():

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

    # parâmetro do p2
    player2 = turtle.Turtle("square")
    player2.speed(0)
    player2.turtlesize(player_height, player_width)
    player2.color("blue")
    player2.penup()
    player2.setx(340)

    # pontuação
    score_1 = 0
    score_2 = 0

    # display de pontuação
    scoreboard = turtle.Turtle("square")
    scoreboard.speed(0)
    scoreboard.color("white")
    scoreboard.penup()
    scoreboard.hideturtle()
    scoreboard.goto(0, 180)
    scoreboard.write("0 : 0", align="center", font=(
        "Press Start 2P", 24, "normal"))

    # display de vitória
    victory = turtle.Turtle("square")
    victory.speed(0)
    victory.color("green")
    victory.penup()
    victory.hideturtle()
    victory.goto(0, 0)

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

    while True:

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
            scoreboard.clear()
            scoreboard.write("{} : {}".format(score_1, score_2),
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
            scoreboard.clear()
            scoreboard.write("{} : {}".format(score_1, score_2),
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

        # colisão da bola com o player 2
        if (ball.xcor() > 320 and ball.ycor() < player2.ycor() + 65 and
                ball.ycor() > player2.ycor() - 65 and
                ball.xcor() < 321):
            ball.dx *= -1
            if (ball.dx > 0):
                ball.dx += 0.01
            elif (ball.dx < 0):
                ball.dx -= 0.01

            # divisão de setores
            if (ball.ycor() <= player2.ycor() + 5 and
                    ball.ycor() >= player2.ycor() - 5):
                if (ball.dy > 0):
                    ball.dy = -ball.dx
                elif (ball.dy < 0):
                    ball.dy = ball.dx

            elif (ball.ycor() > player2.ycor() + 5 and
                  ball.ycor() <= player2.ycor() + 20):
                if (ball.dy > 0):
                    ball.dy = -ball.dx + 0.02
                elif (ball.dy < 0):
                    ball.dy = ball.dx - 0.02

            elif (ball.ycor() < player2.ycor() - 5 and
                  ball.ycor() >= player2.ycor() - 20):
                if (ball.dy > 0):
                    ball.dy = -ball.dx + 0.02
                elif (ball.dy < 0):
                    ball.dy = ball.dx - 0.02

            elif (ball.ycor() > player2.ycor() + 20 and
                  ball.ycor() <= player2.ycor() + 35):
                if (ball.dy > 0):
                    ball.dy = -ball.dx + 0.03
                elif (ball.dy < 0):
                    ball.dy = ball.dx - 0.03

            elif (ball.ycor() < player2.ycor() - 20 and
                  ball.ycor() >= player2.ycor() - 35):
                if (ball.dy > 0):
                    ball.dy = -ball.dx + 0.03
                elif (ball.dy < 0):
                    ball.dy = ball.dx - 0.03

            elif (ball.ycor() > player2.ycor() + 35 and
                  ball.ycor() <= player2.ycor() + 50):
                if (ball.dy > 0):
                    ball.dy = -ball.dx + 0.04
                elif (ball.dy < 0):
                    ball.dy = ball.dx - 0.04

            elif (ball.ycor() < player2.ycor() - 35 and
                  ball.ycor() >= player2.ycor() - 50):
                if (ball.dy > 0):
                    ball.dy = -ball.dx + 0.04
                elif (ball.dy < 0):
                    ball.dy = ball.dx - 0.04

            elif (ball.ycor() > player2.ycor() + 50 and
                  ball.ycor() <= player2.ycor() + 65):
                if (ball.dy > 0):
                    ball.dy = -ball.dx + 0.05
                elif (ball.dy < 0):
                    ball.dy = ball.dx - 0.05

            elif (ball.ycor() < player2.ycor() - 50 and
                  ball.ycor() >= player2.ycor() - 65):
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

        # colisão do player 2 com as paredes
        if (player2.ycor() > 180):
            player2.sety(180)
        if (player2.ycor() < -180):
            player2.sety(-180)

        # condição de vitória player 1
        if (score_1 > 5 and score_1 > score_2 + 1):
            victory.write("Vitória 'P1' ", align="center", font=(
                "Press Start 2p", 24, "normal"))
            time.sleep(5)
            victory.clear()
            victory.hideturtle()
            score_1 = 0
            score_2 = 0
            scoreboard.clear()
            scoreboard.write("0 : 0", align="center", font=(
                "Press Start 2P", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1
            if (ball.dx > 0):
                ball.dx = 0.2
            elif (ball.dx < 0):
                ball.dx = -0.2
            ball.dy = 0.2

        # condição de vitória player 2
        if (score_2 > 5 and score_2 > score_1 + 1):
            victory.write("Vitória 'P2' ", align="center", font=(
                "Press Start 2p", 24, "normal"))
            time.sleep(5)
            victory.clear()
            victory.hideturtle()
            score_1 = 0
            score_2 = 0
            scoreboard.clear()
            scoreboard.write("0 : 0", align="center", font=(
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
