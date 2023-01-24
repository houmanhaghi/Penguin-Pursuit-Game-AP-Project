import os, sys
import pygame
from components.constants import *

# HOW TO CLICK IN PYGAME
# https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection


def login():
    user_text = ''

    pygame.display.set_caption("Login")

    welcome = pygame.font.Font(None, 40).render('WELCOME TO THE PENGUIN GAME', 1, (0, 0, 0))
    happy_penguin = pygame.transform.scale(icon_image,(200,300))
    text_field = pygame.font.Font(None, 24).render('Please Enter Your Name', 1, (0, 0, 0))
    input_rect = pygame.Rect(screen_width // 2 - welcome.get_width() // 2, 2 * screen_height // 4 + 30, 200, 25)
    mouse = pygame.mouse.get_pos()

    active = False

    run = True
    while run:
       for event in pygame.event.get():
            # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

                if screen_width // 2 <= mouse[0] <= screen_width // 2 + 140 and screen_height // 2 <= mouse[1] <= screen_height // 2 + 40:
                    pygame.quit()

            if event.type == pygame.KEYDOWN:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]

                # Unicode standard is used for string
                # formation
                else:
                    user_text += event.unicode

            pygame.display.update()

       screen.blit(background, (0, 0))

       screen.blit(welcome, (screen_width//2 - welcome.get_width()//2, screen_height//8))
       screen.blit(happy_penguin, (5*screen_width // 8 , screen_height // 4))
       screen.blit(text_field, (screen_width // 2 - welcome.get_width() // 2, 2*screen_height // 4))
       color_active = pygame.Color('black')
       color_passive = pygame.Color('white')

       if active:
           color = color_active
       else:
           color = color_passive


       pygame.draw.rect(screen, color, input_rect)

       text_surface = base_font.render(user_text, True, (255, 255, 255))

       screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

       input_rect.w = max(100, text_surface.get_width() + 10)




       if screen_width / 2 <= mouse[0] <= screen_width / 2 + 140 and screen_height / 2 <= mouse[1] <= screen_height / 2 + 40:
           pygame.draw.rect(screen, (0,0,255), [screen_width / 2, screen_height / 2, 140, 40])

       else:
           pygame.draw.rect(screen, (0,255,255), [screen_width / 2, screen_height / 2, 140, 40])




       pygame.display.flip()

       clock.tick(fps)

login()