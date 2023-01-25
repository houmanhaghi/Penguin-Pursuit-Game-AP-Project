import pygame
from components.constants import *
import os, sys
import pygame as py
from assets import *
from db import *

class Wall():

    def __init__(self, position):
        walls.append(self)
        self.rect = pygame.Rect(position[0]+maze_start[0], position[1]+maze_start[1], wall_size, wall_size)



class ColoredPenguin:
    def __init__(self):
        self.rect = pygame.Rect(staff_start[0]+maze_start[0], staff_start[1]+maze_start[1], staff_size, staff_size)

        self.icon_address = pygame.transform.scale(pygame.image.load(
        #dynamic address
        # os.path.join(Path.cwd().parent, r'assets/colored_penguin.png')
        #houman address
        os.path.join(r"C:\Users\rezah\Desktop\comp term 5\py\Advanced-Programming-Project\assets\colored_penguin.png")
        ), (staff_size, staff_size))

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)


    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        global walls
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom


class BlackPenguin(ColoredPenguin):
    def __init__(self):
        super().__init__()

        self.icon_address = pygame.transform.scale(pygame.image.load(
            # dynamic address
            # os.path.join(Path.cwd().parent, r'assets/black_penguin.png')

            # houman address
            os.path.join(
                r"C:\Users\rezah\Desktop\comp term 5\py\Advanced-Programming-Project\assets\black_penguin.png")

        ), (staff_size, staff_size))

    ### penguin movement
    ### it should be in an array and will be different for each level
    def BlackPenguin_move(self, last_level):
        pass


class Fish:
    def __init__(self):
        # self.rect = pygame.Rect(staff_end[0]+maze_start[0], staff_end[1]+maze_start[1], staff_size, staff_size)
        self.icon_address = pygame.transform.scale(pygame.image.load(
        #dynamic address
        # os.path.join(Path.cwd().parent, r'assets/fish.png')

        #houman address
        os.path.join(r"C:\Users\rezah\Desktop\comp term 5\py\Advanced-Programming-Project\assets\fish.png")

        ), (staff_size, staff_size))

    def set_fish_rect(self, position):
        self.rect = pygame.Rect(position[0]+maze_start[0], position[1]+maze_start[1], staff_size, staff_size)


class Maze:
    def __init__(self):
        # maze should be called from other files depends on level
        self.maze = [
            "WWWWWWWWWWWWWWWWWWWWWW",
            "W     WWWW           W",
            "W     WWWW       W   W",
            "W   W          WWWW  W",
            "W WWW    WWWW        W",
            "W   W      W  W      W",
            "W   W      W   WWW  WW",
            "W   WWW W WW   W  W  W",
            "W      W    W   W W  W",
            "W WW   W    WWWWW W  W",
            "W W      W W         W",
            "W  W   WWWW    WWW   W",
            "W     W          W E W",
            "WWWWWWWWWWWWWWWWWWWWWW",
        ]

    def create_maze(self):
        # convert maze into array
        x, y = 0, 0
        for row in self.maze:
            for column in row:
                if column.lower() == 'w':
                    Wall((x, y))
                elif column.lower() == 'e':
                    global staff_end
                    staff_end = (x, y)
                    fish.set_fish_rect((x,y))

                x += staff_size
            y += staff_size
            x = 0


def one_player_game(player_information):

    ### attributes
    global maze_start, maze_size, staff_start, staff_end, staff_size, wall_size
    maze_size = (550, 350)
    maze_start = (screen_width //2 - maze_size[0]//2, 5*screen_height//18)
    staff_start = (32, 32)
    staff_size = 25
    wall_size = 25

    global player_username, player_scores, player_last_level, player_last_result
    player_username, player_scores, player_last_level, player_last_result = player_information

    global walls
    walls = []
    new_level = 1
    new_result = 'loss'


    ### instances
    global colored_penguin, black_penguin, fish
    colored_penguin = ColoredPenguin()
    black_penguin = BlackPenguin()
    fish = Fish()
    maze = Maze()
    maze.create_maze()



    ### control variables
    if player_last_result == 'win':
        if player_last_level < max_level:
            new_level = player_last_level+1
            black_penguin.BlackPenguin_move(player_last_level+1)
    elif player_last_result == 'loss':
        new_level = player_last_level
        black_penguin.BlackPenguin_move(player_last_level)
    elif player_last_result == 'double loss':
        if player_last_level > 1:
            new_level = player_last_level - 1
            black_penguin.BlackPenguin_move(player_last_level-1)



    # pygame starts
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(f"Lumosity")

    # drawers
    show_level = pygame.font.Font(None, 40).render(f'LEVEL {new_level}', True, (0, 0, 0))
    show_level_position = (screen_width//2 - show_level.get_width()//2 ,maze_start[1]//2)

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
            if event.type == pygame.QUIT:
                run = False

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            colored_penguin.move(-2, 0)
        if key[pygame.K_RIGHT]:
            colored_penguin.move(2, 0)
        if key[pygame.K_UP]:
            colored_penguin.move(0, -2)
        if key[pygame.K_DOWN]:
            colored_penguin.move(0, 2)

        # Just added this to make it slightly fun ;)
        if colored_penguin.rect.colliderect(fish.rect):
            pygame.quit()
            sys.exit()

        # draw and blit elements
        screen.blit(background, (0, 0))
        screen.blit(show_level, show_level_position)
        screen.blit(colored_penguin.icon_address, colored_penguin.rect)
        screen.blit(black_penguin.icon_address, black_penguin.rect)
        screen.blit(fish.icon_address, fish.rect)

        for wall in walls:
            pygame.draw.rect(screen, (255, 255, 255), wall.rect)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(fps)


pygame.quit()

#example
one_player_game(('houman', '10, 40, 97', 1, 'win'))