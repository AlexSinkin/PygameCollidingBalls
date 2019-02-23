import pygame as pg
import random as rnd
import sys


def check_exit_event():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()


class Ball:
    def __init__(self, x, y, dx, dy, image):
        print(x, y, dx, dy)
        self.img = pg.transform.scale(image, (150, 150))
        self.dx = dx
        self.dy = dy
        self.rect = screen.blit(self.img, (x, y))
        return

    def show(self):
        screen.blit(self.img, self.rect)

    def move(self):
        self.rect = self.rect.move([self.dx, self.dy])
        self.show()
        return

    def check_collide_with_walls(self, left_x, right_x, top_y, bottom_y):
        if self.rect.left < left_x or self.rect.right > right_x:
            self.dx *= -1

        if self.rect.top < top_y or self.rect.bottom > bottom_y:
            self.dy *= -1
        return
# конец класса.


size = width, height = 1000, 600
white = 255, 255, 255

screen = pg.display.set_mode(size)

circles = ("intro_ball.gif", "football_new.png", "basketball.png")

balls_array = []
balls_n = 10

for i in range(balls_n):
    balls_array.append(Ball(rnd.randint(100, width-100),
                            rnd.randint(100, height-100),
                            rnd.randint(1, 6),
                            rnd.randint(1, 6), pg.image.load(rnd.choice(circles))))

clock = pg.time.Clock()

while True:
    check_exit_event()
    screen.fill(white)

    for ball in balls_array:
        ball.move()
        ball.check_collide_with_walls(0, width, 0, height)

    pg.display.flip()
    clock.tick(70)
