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

def draw_the_ball(window, ball_center):
    window.fill((0, 0, 0))
    pygame.draw.circle(window, (0, 255, 0), ball_center, 10, 0)

def draw_paddles(window):
    x, y = left_paddle_coords
    pygame.draw.rect(window, (0,255,0), (x, y,10,50) ,0)
    pygame.draw.rect(window, (0,255,0), (WIDTH - 60, HEIGHT/2 -25 ,10,50) ,0)

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

def move_left_paddle(direction):
    x, y = left_paddle_coords
    if direction == UP:
        y = y - 1
    elif direction == DOWN:
        y = y + 1
    return (x, y)

while True:
    draw_the_ball(window, ball_center)
    draw_paddles(window)
    ball_center, velocity = new_ball_center()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            print(event.key)
            if event.key == K_w:
                print("I'm working")
                left_paddle_coords = move_left_paddle(UP)
            elif event.key == K_s:
                left_paddle_coords = move_left_paddle(DOWN)
    clock.tick(60)
