import os, sys
import pygame
from pathlib import Path

screen_width, screen_height = 600, 600 # 800, 600
fps= 60 #frame per second
clock = pygame.time.Clock()


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

base_font = pygame.font.Font(None, 20)
font2 = pygame.font.SysFont("gadugi", 25, bold=True)
header_font = pygame.font.SysFont("gadugi", 35, bold=True)
header_font_none = pygame.font.Font(None, 35)

icon_image = pygame.image.load(
    # os.path.join(Path.cwd().parent, r'assets/happy_penguin.png')
    #houman addr
    os.path.join(r"C:\Users\rezah\Desktop\comp term 5\py\Advanced-Programming-Project\assets\happy_penguin.png")
    # miayesh addr
    ##
)
pygame.display.set_icon(icon_image)



background = pygame.transform.scale(pygame.image.load(
    #dynamic address
    # os.path.join(Path.cwd().parent, r'assets/bg1.jpg')

    #houman address
    os.path.join(r"C:\Users\rezah\Desktop\comp term 5\py\Advanced-Programming-Project\assets\bg1.jpg")

    ), (screen_width, screen_height))


max_level = 5