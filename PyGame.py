import pygame as pg
import random as rnd
import sys

size = width, height = 1000, 600

white = 255, 255, 255

screen = pg.display.set_mode(size)

ball = pg.image.load("intro_ball.gif")
ball_1 = ball.get_rect(center=(rnd.randint(200, 400), rnd.randint(200, 400)))
ball_2 = ball.get_rect(center=(rnd.randint(90, 180), rnd.randint(90, 180)))

speed_1 = [2, 2]
speed_2 = [2, 2]

clock = pg.time.Clock()

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

###
    ball_1 = ball_1.move(speed_1)
    if ball_1.left < 0 or ball_1.right > width:
        speed_1[0] = -speed_1[0]

    if ball_1.top < 0 or ball_1.bottom > height:
        speed_1[1] = -speed_1[1]

###
    ball_2 = ball_2.move(speed_2)
    if ball_2.left < 0 or ball_2.right > width:
        speed_2[0] = -speed_2[0]

    if ball_2.top < 0 or ball_2.bottom > height:
        speed_2[1] = -speed_2[1]

###
    screen.fill(white)
    screen.blit(ball, ball_1)
    screen.blit(ball, ball_2)
    pg.display.flip()
    clock.tick(50)

