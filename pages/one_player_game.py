import time
from components.levels import *
from components.constants import *
import os, sys
from db.data_base import *

class Wall():

    def __init__(self, position):
        walls.append(self)
        self.rect = pygame.Rect(position[0]+maze_start[0], position[1]+maze_start[1], wall_size, wall_size)



class ColoredPenguin:
    def __init__(self):
        self.rect = pygame.Rect(staff_start[0]+maze_start[0], staff_start[1]+maze_start[1], staff_size, staff_size)
        self.footprint = set()

        #dynamic address
        # os.path.join(Path.cwd().parent, r'assets/colored_penguin.png')
        try:
            self.icon_address = pygame.transform.scale(pygame.image.load(
            os.path.join(r"C:\Users\rezah\Desktop\comp term 5\py\Advanced-Programming-Project\assets\colored_penguin.png")
            ), (staff_size, staff_size))
        except:
            self.icon_address = pygame.transform.scale(pygame.image.load(
            os.path.join(r"C:\Users\USER\Desktop\nia\AP\project\Advanced-Programming-Project\assets\colored_penguin.png")
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
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                    self.footprint.add((self.rect.x, self.rect.y))
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                    self.footprint.add((self.rect.x, self.rect.y))
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                    self.footprint.add((self.rect.x, self.rect.y))
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
                    self.footprint.add((self.rect.x, self.rect.y))


class BlackPenguin(ColoredPenguin):
    def __init__(self):
        super().__init__()
        self.temp = []

        # dynamic address
        # os.path.join(Path.cwd().parent, r'assets/black_penguin.png')
        try:
            self.icon_address = pygame.transform.scale(pygame.image.load(
            os.path.join(
                r"C:\Users\rezah\Desktop\comp term 5\py\Advanced-Programming-Project\assets\black_penguin.png")
                ), (staff_size, staff_size))
        except:
            self.icon_address = pygame.transform.scale(pygame.image.load(
            os.path.join(r"C:\Users\USER\Desktop\nia\AP\project\Advanced-Programming-Project\assets\black_penguin.png")
            ), (staff_size, staff_size))


    ### penguin movement
    ### it should be in an array and will be different for each level
    def BlackPenguin_move(self, last_step):

        # this numbers are for level 1:
        global _last_step, total_steps, total_time
        _last_step = last_step
        total_steps = 30
        total_time = 30 #second
        step = (total_steps * wall_size // total_time)

        # up, right, down, left
        u, r, d, l, = (0, -step), (step, 0), (0, step), (-step, 0)
        movement_steps =[
            r,r,r,r,d,d,r,r,r,r,r,r,r,r,r,d,r,r,r,r,r,d,d,d,d,d,d,d,d
        ]
        if not last_step in self.temp:
            if len(self.temp) == 0:
                self.rect.x -= 4
                self.rect.y -= 4
            self.temp.append(last_step)
            self.rect.x += movement_steps[last_step][0]
            self.rect.y += movement_steps[last_step][1]

class Fish:
    def __init__(self):
        #dynamic address
        # os.path.join(Path.cwd().parent, r'assets/fish.png')

        try:
            self.icon_address = pygame.transform.scale(pygame.image.load(
            os.path.join(r"C:\Users\rezah\Desktop\comp term 5\py\Advanced-Programming-Project\assets\fish.png")

            ), (staff_size, staff_size))
        except:
            self.icon_address = pygame.transform.scale(pygame.image.load(
            os.path.join(r"C:\Users\USER\Desktop\nia\AP\project\Advanced-Programming-Project\assets\fish.png")
            ), (staff_size, staff_size))

    def set_fish_rect(self, position):
        self.rect = pygame.Rect(position[0]+maze_start[0], position[1]+maze_start[1], staff_size, staff_size)


class Maze:
    def __init__(self):
        # maze should be called from other files depends on level
        self.maze = level_maze

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

    #if staff_size == wall_size: walls will not be discrites
    staff_size = 25
    wall_size = 25

    try:
        db = DB(r'C:\Users\rezah\Desktop\comp term 5\py\Advanced-Programming-Project\db\members.db')
    except:
        db = DB(r"C:\Users\USER\Desktop\nia\AP\project\Advanced-Programming-Project\db\members.db")


    global player_username, player_scores, player_last_level, player_last_result
    # player_information = db.read(player_information)
    player_username, player_scores, player_last_level, player_last_result = player_information[0], player_information[1], player_information[2], player_information[3],

    global walls, score, new_result, new_level, coloredPenguin_footprint
    walls = []
    h = 0
    new_h = -1

    ### control variables
    if player_last_result == 'win':
        if player_last_level < max_level:
            new_level = player_last_level+1
            # black_penguin.BlackPenguin_move(player_last_level+1)
    elif player_last_result == 'loss':
        new_level = player_last_level
        # black_penguin.BlackPenguin_move(player_last_level)
    elif player_last_result == 'double loss':
        if player_last_level > 1:
            new_level = player_last_level - 1
            # black_penguin.BlackPenguin_move(player_last_level-1)
    else:
        new_level = 1

    ##### level dependecies #######
    global black_penguin_speed, rotation_time, level_maze
    black_penguin_speed = levels[new_level-1]['black_penguin_speed']
    rotation_time = levels[new_level-1]['rotation_time']
    level_maze = levels[new_level-1]['level_maze']


    ### instances
    global colored_penguin, black_penguin, fish
    colored_penguin = ColoredPenguin()
    black_penguin = BlackPenguin()
    fish = Fish()
    maze = Maze()
    maze.create_maze()

    # pygame starts
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(f"Lumosity")

    # os.path.join(Path.cwd().parent, r'assets/happy_penguin.png')
    try:
        icon_image = pygame.image.load(
            os.path.join(
                r"C:\Users\rezah\Desktop\comp term 5\py\Advanced-Programming-Project\assets\happy_penguin.png"))
        pygame.display.set_icon(icon_image)
    except:
        icon_image = pygame.image.load(
            os.path.join(
                r"C:\Users\USER\Desktop\nia\AP\project\Advanced-Programming-Project\assets\happy_penguin.png"))
        pygame.display.set_icon(icon_image)

    # drawers
    show_level = pygame.font.Font(None, 40).render(f'LEVEL {new_level}', True, (0, 0, 0))
    show_level_position = (screen_width//2 - show_level.get_width()//2 ,maze_start[1]//2)

    run = True
    step_counter = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
            if event.type == pygame.QUIT:
                run = False

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            colored_penguin.move(-2, 0)
        if key[pygame.K_RIGHT]or key[pygame.K_d]:
            colored_penguin.move(2, 0)
        if key[pygame.K_UP]or key[pygame.K_w]:
            colored_penguin.move(0, -2)
        if key[pygame.K_DOWN]or key[pygame.K_s]:
            colored_penguin.move(0, 2)

        # Just added this to make it slightly fun ;)
        if colored_penguin.rect.colliderect(fish.rect):
            score = ( len(colored_penguin.footprint)//3 + total_steps - _last_step)
            new_player_score = player_scores + f', {score}'
            db.update((player_username, new_player_score, new_level, 'win'))
            time.sleep(1)
            pygame.quit()
            sys.exit()

        if black_penguin.rect.colliderect(fish.rect):
            time.sleep(1)
            if player_last_result == 'win':
                db.update((player_username, player_scores, new_level, 'loss'))
            elif player_last_result == 'loss' or player_last_level == 'double loss':
                db.update((player_username, player_scores, new_level, 'double loss'))
            else:
                db.update((player_username, player_scores, new_level, 'loss'))
            pygame.quit()
            sys.exit()


        #blach penguin movement
        try:
            black_penguin.BlackPenguin_move(black_penguin_speed * step_counter // fps)
        except:
            pass
        finally:
            step_counter += 1

        # rotation control
        h = 90 * (step_counter // (fps * rotation_time))
        if h != new_h:
            new_h = h

        # draw and blit elements

######### whit screen rotation
        screen.blit(background, (0, 0))
        if rotation_time > step_counter // fps:
            screen.blit(show_level, show_level_position)
        else:
            screen.blit(pygame.transform.scale(pygame.image.load(
                r'C:\Users\rezah\Desktop\comp term 5\py\Advanced-Programming-Project\assets\up_direction.png'
            ), (50, 60))
                , ( screen_width // 2 - 20, walls[0].rect.y - 60))
        screen.blit(pygame.transform.rotate(colored_penguin.icon_address, h), colored_penguin.rect)
        screen.blit(pygame.transform.rotate(black_penguin.icon_address, h), black_penguin.rect)
        screen.blit(pygame.transform.rotate(fish.icon_address, h), fish.rect)
        for wall in walls:
            pygame.draw.rect(screen, (255, 255, 255), wall.rect)

        screen.blit(pygame.transform.rotate(screen, -h), (0, 0))

#########################################################################

        pygame.display.update()
        pygame.display.flip()
        clock.tick(fps)


pygame.quit()

#example
one_player_game(('houman', '10, 40, 97, 876', 1, 'win'))