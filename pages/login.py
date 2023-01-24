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
    input_rect = pygame.Rect(screen_width // 2 - welcome.get_width() // 2 , 2 * screen_height // 4 + 30, 300, 25)
    login_rect = pygame.Rect(screen_width // 2 - welcome.get_width() // 2 + 50 , 2*screen_height // 4 + text_field.get_height()+ 60,100 ,30)
    login_button = pygame.font.Font(None, 20).render('Login', True, (0, 0, 0))
    signup_rect = pygame.Rect(screen_width // 2 - welcome.get_width() // 2 + 50,login_rect.y + 40, 100, 30)
    Signup_button = pygame.font.Font(None, 20).render('Signup', True, (0, 0, 0))

    active = False
    run = True
    command = None

    while run:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if  login_rect.x < mouse[0] < login_rect.x+ 100 and login_rect.y <= mouse[1] <= login_rect.y+ 30:
                    pass

                elif  signup_rect.x < mouse[0] < signup_rect.x+ 100 and signup_rect.y <= mouse[1] <= signup_rect.y+ 30:
                    pass

                elif input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False



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
        screen.blit(text_field, (screen_width // 2 - welcome.get_width() // 2 +6, 2*screen_height // 4))
        color_active = pygame.Color('black')
        color_passive = pygame.Color('white')

        if active:
           color = color_active
        else:
           color = color_passive


        pygame.draw.rect(screen, color, input_rect)
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(200, text_surface.get_width() + 10)


        pygame.draw.rect(screen, (0,0,180),login_rect)
        screen.blit(login_button, (login_rect.x + 32 , login_rect.y + 9))
        pygame.draw.rect(screen, (0, 0, 180), signup_rect)
        screen.blit(Signup_button, (signup_rect.x + 27, signup_rect.y + 9))


        pygame.display.flip()

        clock.tick(fps)

        if command:
            pass




login()