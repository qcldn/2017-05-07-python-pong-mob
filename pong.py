import pygame, sys
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

WIDTH = 600
HEIGHT = 400
UP = 1
DOWN = -1

window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Pong')

ball_center = (300, 200)
velocity = (-1, 1)
left_paddle_coords = (50, 175)
right_paddle_coords = (540, 175)

def draw_the_ball(window, ball_center):
    window.fill((0, 0, 0))
    pygame.draw.circle(window, (0, 255, 0), ball_center, 10, 0)

def draw_paddles(window):
    x, y = left_paddle_coords
    a, b = right_paddle_coords
    pygame.draw.rect(window, (0,255,0), (x, y, 10,50) ,0)
    pygame.draw.rect(window, (0,255,0), (a, b ,10,50) ,0)

def new_ball_center():
    (x, y) = ball_center
    (dx, dy) = velocity
    ball_center_the_second = (x + dx, y + dy)
    velocity_the_second = detect_collision(ball_center_the_second)
    return ball_center_the_second, velocity_the_second

def detect_collision(ball_center):
    (x, y) = ball_center
    (dx, dy) = velocity
    if y == 0 or y == 400:
        dy = dy*-1
    return (dx, dy)

def move_paddle(coords,direction):
    x, y = coords
    if direction == UP:
        if y != 0:
            y = y - 1
    elif direction == DOWN:
        if y != HEIGHT - 50:
            y = y + 1
    return (x, y)

def detect_hit(paddle_coords):
    pass

while True:
    draw_the_ball(window, ball_center)
    draw_paddles(window)
    ball_center, velocity = new_ball_center()
    pygame.display.update()
    for event in pygame.event.get():
        pass
    pressed = pygame.key.get_pressed()
    if pressed[K_w]:
        left_paddle_coords = move_paddle(left_paddle_coords,UP)
    elif pressed[K_s]:
        left_paddle_coords = move_paddle(left_paddle_coords,DOWN)
    if pressed[K_UP]:
        right_paddle_coords = move_paddle(right_paddle_coords,UP)
    elif pressed[K_DOWN]:
        right_paddle_coords = move_paddle(right_paddle_coords,DOWN)
    clock.tick(60)
