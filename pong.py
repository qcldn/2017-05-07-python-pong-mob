import pygame, sys
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

WIDTH = 600
HEIGHT = 400

window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Pong')

ball_center = (300, 200)
velocity = (-1, 1)

def draw_the_ball(window, ball_center):
    pygame.draw.circle(window, (0, 255, 0), ball_center, 10, 0)

def new_ball_center():
    (x, y) = ball_center
    (dx, dy) = velocity
    return (x + dx, y + dy)

while True:
    draw_the_ball(window, ball_center)
    ball_center = new_ball_center()
    pygame.display.update()
    for event in pygame.event.get():
        pass
    clock.tick(60)
