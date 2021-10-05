
import pygame
from pygame.locals import *
from typer.colors import YELLOW, RED, GREEN, BLACK, MAGENTA, WHITE, BLUE, CYAN

pygame.init()
screen = pygame.display.set_mode((400, 500))
done = False
background=YELLOW
key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE,
    K_y:YELLOW, K_c:CYAN, K_m:MAGENTA, K_w:WHITE}


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]

    caption = "vishal"
    pygame.display.set_caption(caption)
    screen.fill(background)
    pygame.display.update()
