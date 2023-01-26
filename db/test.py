import sqlite3 as sq
from data_base import *
import pygame, sys
from pygame.locals import *
from components.constants import *

def score_table(player):

     D = DB('members.db')
     d = D.read(player)

     name , last_level = d[0],  d[2]
     print(name, last_level)

     print(d)
     arr = d[1].split(",")
     int_arr = list(map(int, arr))
     for i in range(len(int_arr)):
          # arr[i] = int(arr[i])
          score = max(int_arr)

     print(max(arr))

     mainClock = pygame.time.Clock()
     pygame.init()
     pygame.display.set_caption('Penguin Pursuit')


     """
     A function that can be used to write text on our screen and buttons
     """
     def draw_text(text, font2, color, surface, x, y):
          textobj = font2.render(text, 1, color)
          textrect = textobj.get_rect()
          textrect.topleft = (x, y)
          surface.blit(textobj, textrect)

     # A variable to check for the status later
     click = False

     # Main container function that holds the buttons and game functions

     def main_menu():
          global clock
          while True:
               screen.blit(background, (0, 0))
               table = pygame.image.load(
                    # dynamic address
                    # os.path.join(Path.cwd().parent, r'assets/bg1.jpg')

                    # houman address
                    # os.path.join(r"C:\Users\rezah\Desktop\comp term 5\py\Advanced-Programming-Project\assets\table.png")
                    #
                    # ), (screen_width, screen_height))
                    # nia address
                    os.path.join(r"C:\Users\USER\Desktop\nia\AP\project\Advanced-Programming-Project\assets\table.png")
               )
               screen.blit(table, (50,300))

               draw_text('Score Table', header_font, (0, 0, 0), screen, screen_width // 2 - 90, 215)

               mx, my = pygame.mouse.get_pos()
               # creating exit button
               exit_button= pygame.Rect(screen_width - 100, 535, 60, 30)


               if exit_button.collidepoint((mx, my)):
                    if click:
                         return None

               pygame.draw.rect(screen, (0, 0,0), exit_button)

               # making the table
               draw_text('Name', font2, (255, 255, 255), screen, screen_width // 4 - 25, 305)
               draw_text('Best Score', font2, (255, 255, 255), screen, screen_width - 323, 305)
               draw_text('Level', font2, (255, 255, 254), screen, screen_width - 150, 305)
               draw_text(str(name), table_font, (0, 0, 0), screen, screen_width // 4 - 30, 346)
               draw_text(str(score), table_font, (0, 0, 0), screen, screen_width - 275, 346)
               draw_text(str(last_level), table_font, (0, 0, 0), screen, screen_width - 130, 346)

               # writing text on the button
               draw_text('Quit', font2, (255, 255, 255), screen, screen_width - 96, 530)


               click = False


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

     main_menu()


score_table(("houman", "0, 10, 23, 4, 76, 23", 1, "null"))
# score_table(("niaw", "30", 3, "win"))
# start_menu(("hello", "23, 45, 80", 1, "win"))
