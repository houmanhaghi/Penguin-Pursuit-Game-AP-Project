import os, sys
import pygame
from pathlib import Path
from pygame.locals import *
import sqlite3 as sq
import time



##################################### constants ########################################
screen_width, screen_height = 600, 600 # 800, 600
fps= 60 #frame per second
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

base_font = pygame.font.Font(None, 20)
font2 = pygame.font.SysFont("gadugi", 25, bold=True)
header_font = pygame.font.SysFont("gadugi", 35, bold=True)
table_font = pygame.font.SysFont("gadugi", 20, bold=True)

# os.path.join(Path.cwd().parent, r'assets/happy_penguin.png')
try:
    icon_image = pygame.image.load(
    os.path.join(r"C:\Users\rezah\Desktop\comp term 5\py\Advanced-Programming-Project\assets\happy_penguin.png"))
    pygame.display.set_icon(icon_image)
except:
    icon_image = pygame.image.load(
    os.path.join(r"C:\Users\USER\Desktop\nia\AP\project\Advanced-Programming-Project\assets\happy_penguin.png"))
    pygame.display.set_icon(icon_image)


#dynamic address
# os.path.join(Path.cwd().parent, r'assets/bg1.jpg')

try:
    background = pygame.transform.scale(pygame.image.load(
    os.path.join(r"C:\Users\rezah\Desktop\comp term 5\py\Advanced-Programming-Project\assets\bg1.jpg")
    ), (screen_width, screen_height))

except:
    background = pygame.transform.scale(pygame.image.load(
    os.path.join(r"C:\Users\USER\Desktop\nia\AP\project\Advanced-Programming-Project\assets\bg1.jpg")
    ), (screen_width, screen_height))


max_level = 5




levels = [
    # level 1
{
    'rotation_time' : 5,
    'black_penguin_speed' : 1,
    'level_maze':   # 22 * 14
                    [
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
                        ],


    } ,
# level 2
{
    'rotation_time' : 2,
    'black_penguin_speed' : 1,
    'level_maze':   # 22 * 14
                    [
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
                        ],


    } ,
# level 3
{
    'rotation_time' : 2,
    'black_penguin_speed' : 2,
    'level_maze':   # 22 * 14
                    [
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
                        ],


    } ,

# level 4
{
    'rotation_time' : 2,
    'black_penguin_speed' : 2,
    'level_maze':   # 22 * 14
                    [
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
                        ],


    } ,
# level 5
{
    'rotation_time' : 2,
    'black_penguin_speed' : 2,
    'level_maze':   # 22 * 14
                    [
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
                        ],


    } ,

]

##################################### data base #######################################
class DB:
    def __init__(self, data_base_file):
        self.data_base_file = data_base_file
        # self.connect = sq.connect(self.data_base_file)
        try:
            self.connect = sq.connect(r"C:\Users\rezah\Desktop\comp term 5\py\Advanced-Programming-Project\db\members.db")
        except:

            self.connect = sq.connect(r"C:\Users\USER\Desktop\nia\AP\project\Advanced-Programming-Project\db\members.db")
        self.cursor = self.connect.cursor()


    def read(self, info: str):
        self.cursor.execute("SELECT * FROM ALL_MEMBERS")
        result = self.cursor.fetchall()

        for line in result:
            if line[0] == info or line[0] == info[0]:
                return line
        # line -> name, scores, last_level, last_result
        # name : name
        # score: ex) 34, 5, 54
        # last_level: 3
        # last_result: "win" or "loss" or "double loss"


    def insert(self, info:tuple):
        self.cursor.execute("INSERT INTO ALL_MEMBERS VALUES ( ? , ? , ? , ? )", info)
        self.connect.commit()


    def update(self, info):
        # first delete then insert :)
        # self.cursor.execute(f"""
        #                 DELETE FROM ALL_MEMBERS
        #                 WHERE username = '{info[0]}';
        #                 """)
        #
        # self.cursor.execute("INSERT INTO ALL_MEMBERS VALUES ( ? , ? , ? , ? )", info)

        self.cursor = self.connect.cursor()
        self.cursor.execute(f'''
                UPDATE ALL_MEMBERS
                SET scores = "{info[1]}", lase_level = {info[2]}, last_result = "{info[3]}"
                WHERE username = "{info[0]}" ;
        ''')

        self.connect.commit()



##################################### login ############################################
def login():
    username = ''
    db = DB(r'C:\Users\rezah\Desktop\comp term 5\py\Advanced-Programming-Project\db\members.db')
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Login")
####
    welcome = pygame.font.Font(None, 40).render('WELCOME TO THE PENGUIN GAME', True, (0, 0, 0))
    happy_penguin = pygame.transform.scale(icon_image,(200,300))
    text_field = pygame.font.Font(None, 24).render('Please Enter Your Name', True, (0, 0, 0))
    input_rect = pygame.Rect(screen_width // 2 - welcome.get_width() // 2 + 20, 2 * screen_height // 4 , 300, 25)
    login_rect = pygame.Rect(screen_width // 2 - welcome.get_width() // 2 + 50 + 20, 2*screen_height // 4 + text_field.get_height()+ 30 ,100 ,30)
    login_button = pygame.font.Font(None, 20).render('Login', True, (0, 0, 0))
    signup_rect = pygame.Rect(screen_width // 2 - welcome.get_width() // 2 + 50 + 20,login_rect.y + 45 , 100, 30)
    Signup_button = pygame.font.Font(None, 20).render('Signup', True, (0, 0, 0))

    active = False
    run = True

    while run:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if  login_rect.x < mouse[0] < login_rect.x+ 100 and login_rect.y <= mouse[1] <= login_rect.y+ 30:
                    return db.read(username)

                elif  signup_rect.x < mouse[0] < signup_rect.x+ 100 and signup_rect.y <= mouse[1] <= signup_rect.y+ 30:
                    db.insert((username, 0, 1, None))
                    return db.read(username)

                elif input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False



            if event.type == pygame.KEYDOWN:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    username = username[:-1]

                # Unicode standard is used for string
                # formation
                else:
                    username += event.unicode

        pygame.display.update()

        screen.blit(background, (0, 0))

        screen.blit(welcome, (screen_width//2 - welcome.get_width()//2, screen_height//8))
        screen.blit(happy_penguin, (17 * screen_width // 32 , 9 * screen_height // 32))
        screen.blit(text_field, (screen_width // 2 - welcome.get_width() // 2 +6 + 20, 2*screen_height // 4 - 40))
        color_active = pygame.Color('black')
        color_passive = pygame.Color('white')

        if active:
           color = color_active
        else:
           color = color_passive


        pygame.draw.rect(screen, color, input_rect)
        text_surface = pygame.font.Font(None, 24).render(username, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect.x + 5 + 20, input_rect.y + 5))
        input_rect.w = max(200, text_surface.get_width() + 10)


        pygame.draw.rect(screen, (0,0,180),login_rect)
        screen.blit(login_button, (login_rect.x + 32 , login_rect.y + 9))
        pygame.draw.rect(screen, (0, 0, 180), signup_rect)
        screen.blit(Signup_button, (signup_rect.x + 27, signup_rect.y + 9))


        pygame.display.flip()
        clock.tick(fps)



########################################### menu ################################################## 
def start_menu(player_information : tuple):
    # player_name, player_scores, player_last_level, player_last_result  = player_information[0], player_information[1], player_information[2], player_information[3]

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    mainClock = pygame.time.Clock()
    pygame.display.set_caption('Penguin Pursuit')

    # setting font2 settings

    """
    A function that can be used to write text on our screen and buttons
    """

    # A variable to check for the status later
    click = False

    # Main container function that holds the buttons and game functions
    global clock
    while True:
        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # creating buttons

        button_1 = pygame.Rect(screen_width // 2 - 100, 250, 200, 50)
        button_2 = pygame.Rect(screen_width // 2 - 100, 350, 200, 50)
        button_3 = pygame.Rect(screen_width // 2 - 100, 450, 200, 50)
        main_exit_button = pygame.Rect(screen_width - 110, 530, 80, 40)
        # defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                return 'one_player_game'
        if button_2.collidepoint((mx, my)):
            if click:
                return 'two_player_game'
        if button_3.collidepoint((mx, my)):
            if click:
                return 'score_table'
        if main_exit_button.collidepoint((mx, my)):
            if click:
                return 'exit'


        # draw & blit
        screen.blit(background, (0, 0))
        screen.blit(header_font.render("Main Menu", True, (0, 0, 0)), (screen_width // 2 - 95, 117))

        pygame.draw.rect(screen, (0, 191, 255), button_1)
        pygame.draw.rect(screen, (0, 191, 255), button_2)
        pygame.draw.rect(screen, (0, 191, 255), button_3)
        pygame.draw.rect(screen, (220, 11, 0), main_exit_button)

        screen.blit(font2.render("One Player", True, (255, 255, 255)), (screen_width // 2 - 65, 257))
        screen.blit(font2.render('Two Player', True, (255, 255, 255)), (screen_width // 2 - 65, 357))
        screen.blit(font2.render('Score Table', True, (255, 255, 255)), (screen_width // 2 - 65, 457))
        screen.blit(font2.render('Exit', True, (255, 255, 255)), (screen_width - 92, 532))



        pygame.display.update()
        mainClock.tick(60)





######################################### one player game ######################################
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
    player_information = db.read(player_information)
    player_username, player_scores, player_last_level, player_last_result = player_information[0],player_information[1],player_information[2],player_information[3]
    global walls, score, new_result, new_level, coloredPenguin_footprint
    walls = []
    h = 0
    new_h = -1

    ### control variables
    if player_last_result == 'win':
        if player_last_level < max_level:
            new_level = player_last_level+1
        else:
            new_level = player_last_level
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
            # pygame.quit()
            # sys.exit()
            return

        if black_penguin.rect.colliderect(fish.rect):
            time.sleep(1)
            if player_last_result == 'win':
                db.update((player_username, player_scores, new_level, 'loss'))
            elif player_last_result == 'loss' or player_last_level == 'double loss':
                db.update((player_username, player_scores, new_level, 'double loss'))
            else:
                db.update((player_username, player_scores, new_level, 'loss'))
            return
            # pygame.quit()
            # sys.exit()


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

############## whit screen rotation ##################
        
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

######################################################

        pygame.display.update()
        pygame.display.flip()
        clock.tick(fps)


# pygame.quit()



#example
# one_player_game(('houman', '10, 40, 97, 876', 1, 'win'))




########################################### two player game ####################################
def two_player_game(player):
    pass




############################################### score table ####################################
def score_table(player):
     try:
          D = DB(r'C:\Users\rezah\Desktop\comp term 5\py\Advanced-Programming-Project\db\members.db')
     except:
          D = DB(r"C:\Users\USER\Desktop\nia\AP\project\Advanced-Programming-Project\db\members.db")
     d = D.read(player)
     name , last_level = d[0],  d[2]

     if len(name) > 16:
         name = name[:16]

     arr = d[1].split(",")
     int_arr = list(map(int, arr))
     for i in range(len(int_arr)):
          score = max(int_arr)

     mainClock = pygame.time.Clock()
     pygame.init()
     pygame.display.set_caption('Penguin Pursuit')


     """
     A function that can be used to write text on our screen and buttons
     """
     def _draw_text(text, font2, color, surface, x, y):
          textobj = font2.render(text, 1, color)
          textrect = textobj.get_rect()
          textrect.topleft = (x, y)
          surface.blit(textobj, textrect)

     # A variable to check for the status later
     click = False

     # Main container function that holds the buttons and game functions

     global clock
     while True:
         screen.blit(background, (0, 0))

         # dynamic address
         # os.path.join(Path.cwd().parent, r'assets/bg1.jpg')
         try:
             table = pygame.image.load(
                 os.path.join(r"C:\Users\rezah\Desktop\comp term 5\py\Advanced-Programming-Project\assets\table.png"))
         except:
             table = pygame.image.load(
                 os.path.join(r"C:\Users\USER\Desktop\nia\AP\project\Advanced-Programming-Project\assets\table.png"))

         screen.blit(table, (50, 300))

         _draw_text('Score Table', header_font, (0, 0, 0), screen, screen_width // 2 - 90, 215)

         mx, my = pygame.mouse.get_pos()
         # creating exit button
         exit_button = pygame.Rect(screen_width - 110, 530, 80, 40)

         if exit_button.collidepoint((mx, my)):
             if click:
                 return None

         pygame.draw.rect(screen, (220, 11, 0), exit_button)

         # making the table
         _draw_text('Name', font2, (255, 255, 255), screen, screen_width // 4 - 95, 305) # last width: screen_width // 4 - 20
         _draw_text('Best Score', font2, (255, 255, 255), screen, screen_width - 323, 305)
         _draw_text('Level', font2, (255, 255, 254), screen, screen_width - 155, 305)
         _draw_text(str(name), table_font, (0, 0, 0), screen, screen_width // 4 - 90, 346)
         _draw_text(str(score), table_font, (0, 0, 0), screen, screen_width - 275, 346)
         _draw_text(str(last_level), table_font, (0, 0, 0), screen, screen_width - 125, 346)

         # writing text on the button
         _draw_text('Back', font2, (255, 255, 255), screen, screen_width - 96, 530)

         for event in pygame.event.get():
             if event.type == QUIT:
                 pygame.quit()
                 sys.exit()
             if event.type == KEYDOWN:
                 if event.key == K_ESCAPE:
                     pygame.quit()
                     sys.exit()
             if event.type == MOUSEBUTTONDOWN:
                 if event.button == 1:
                     click = True

         pygame.display.update()
         mainClock.tick(60)







############################################ main ############################################### 

def main():
    player_information = login()

    if player_information is None:
        raise FileExistsError('Your Username Doed Not Exist In db')

    while True:
        player_command = start_menu(player_information)

        if player_command == 'one_player_game':
            one_player_game(player_information)
        elif player_command == 'two_player_game':
            two_player_game(player_information)
        elif player_command == 'score_table':
            score_table(player_information)
        elif player_command == 'exit':
            break


if __name__ == '__main__':
    main()